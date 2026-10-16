# Z Potentials English Interview Skill

将英文访谈视频、播客或逐字稿编译为Z Potentials中文深度访谈文章的Codex Skill。

只处理英文访谈，不处理人物传记、Product产品稿、英文博客编译或一般原创文章。

## 交付内容

- 完整英文原稿Word。
- 一句英文、一句中文的中英对照Word。
- 按深度SOP整理的中文成品Word，包括封面、至少四张正文图、同正文格式的图片描述、署名及完整声明；图片出处另存项目资料，不在图下显示来源链接。
- 三个候选标题、原题译文，以及实际审核结果和待确认事项。

流程包含原文核对、口语整理、专业术语解释、分阶段经验自检、经授权的豆包全文审查和实际页面检查。局部返修另存修改稿，不覆盖作者手动修改。

## 安装

让Codex使用技能安装器，从以下仓库安装`skills/zpotentials-depth-interview`目录：

```text
请使用$skill-installer，从https://github.com/chenpen111/zpotentials-english-interview-skill
安装skills/zpotentials-depth-interview这个Skill。
不要覆盖同名技能；如果已经安装，先告诉我。
```

也可以下载仓库，将`skills/zpotentials-depth-interview`整个文件夹放到本机技能目录。务必保留全部参考文件和脚本，不要只复制SKILL.md。

## 调用

```text
请使用$zpotentials-depth-interview编译这期英文访谈。
视频链接：本期链接
编译署名：本期实际作者姓名
输出目录：本次项目目录
允许将本期拟发布的完整中文稿提交豆包审查。
```

仅有视频链接时先寻找可用英文文字稿；素材、登录、关键译义或转载授权不足时需要作者介入。

## 配置与使用边界

完整说明见[Skill使用说明](skills/zpotentials-depth-interview/README.md)，执行入口见[SKILL.md](skills/zpotentials-depth-interview/SKILL.md)。

- 署名按本次任务或个人配置提供；公共版本不含任何人的默认署名。
- 个人配置`profile.local.json`不应提交；团队规则与本期临时例外分开维护。
- Skill不附带豆包账号、浏览器会话或文档渲染服务。工具不可用时必须明确报告，不能虚报审核或排版检查完成。
- 这是可复用工作规范及验收脚本，不是独立的一键翻译软件。
- 本地Skill、GitHub仓库和已下载的副本不自动同步；维护者验证后提交并推送，使用者需更新自己的安装副本。

## 验证

当前分享版本为1.0.0。脚本需要Python3.10以上，验收依赖python-docx1.2.0以上，模拟测试另需Pillow。

```text
python skills/zpotentials-depth-interview/scripts/lint_experience.py
python skills/zpotentials-depth-interview/scripts/test_audit.py
```

测试只验证配置和静态验收条件，不代表已经完成某期访谈的翻译、真实豆包审核或逐页视觉检查。
