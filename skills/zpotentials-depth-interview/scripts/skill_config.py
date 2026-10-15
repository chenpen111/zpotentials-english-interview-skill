"""Resolve team defaults and a local compiler credit without changing files."""

import argparse
import json
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]


def load_rules(profile=None, compiler=None, *, use_local=True):
    rules = json.loads((SKILL / 'references/rules.json').read_text(encoding='utf-8'))
    path = Path(profile) if profile else SKILL / 'profile.local.json'
    if profile or (use_local and path.is_file()):
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        if not isinstance(data, dict) or set(data) - {'compiler'}:
            raise ValueError('Profile must be an object containing only compiler.')
        rules.update(data)
    if compiler is not None:
        rules['compiler'] = compiler
    value = rules.get('compiler')
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Compiler credit is required. Set --compiler or a profile compiler value.')
    value = value.strip()
    if len(value) > 80 or any(c in value for c in '\r\n\x00{}<>'):
        raise ValueError('Compiler must be a single plain-text name of at most 80 characters.')
    if value in {'你的名字', '姓名', 'Your Name', 'YOUR_NAME', 'TODO'}:
        raise ValueError('Replace the example compiler name with the actual approved credit.')
    rules['compiler'] = value
    return rules


def render_footer(rules):
    template = (SKILL / 'references' / rules['footer_file']).read_text(encoding='utf-8')
    if template.count('{compiler}') != 1:
        raise ValueError('Footer template must contain exactly one compiler placeholder.')
    return template.replace('{compiler}', rules['compiler'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', type=Path)
    parser.add_argument('--compiler')
    parser.add_argument('--footer', action='store_true', help='Print the resolved publication footer.')
    args = parser.parse_args()
    try:
        rules = load_rules(args.profile, args.compiler)
        result = render_footer(rules) if args.footer else json.dumps(rules, ensure_ascii=False, indent=2)
    except (OSError, ValueError) as exc:
        parser.exit(2, f'Configuration error: {exc}\n')
    print(result)


if __name__ == '__main__':
    main()
