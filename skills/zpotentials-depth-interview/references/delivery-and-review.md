# 交付和验收

## 文件与版本

每期在用户项目下建立一个清楚命名的子目录。至少分开`source`、`working`、`images`、`qa`、`deliverables`，原始资料不覆盖。`deliverables`固定三份DOCX：英文原稿、中英文对照稿、中文成品稿。新增版本沿用项目边界，先检查用户是否已手改。

署名从本次明确要求、项目配置、个人本地配置依次解析，不能用共享包作者的姓名。配置只支持`compiler`；项目文件通过`--profile`传入，本期直接署名通过`--compiler`传入。用`scripts/skill_config.py --compiler <姓名> --footer`得到准确文末。团队规则和本期例外分别记录，不混淆。

英文：完整核对后的实际对话、说话人、真实可得时间戳；清理转写标记，不补造缺失台词。原始网页/字幕另存source。若确实无法取得时间戳，在项目记录声明，不伪造时间。

双语：逐句英文紧接中文，按原发言顺序；保留用于核对的完整英文，而非仅用缩短后的中文倒译。建议给英文/中文句子设置Word段落样式`EnglishSentence`和`ChineseTranslation`，只是隐藏语义样式，不在正文加“英文/中文”标签。源稿无信息口语的省略/合并要可回查；句子不宜拆到无法理解。

中文：深度SOP完整结构、正文人物名字加冒号、没有时间戳、至少四图加封面、图下仅图片描述、固定署名与声明。图注字体字号颜色同正文、不加粗，不显示图片来源及链接。开头和结尾不缺失，批注不显示为观众正文。

开头按标题、`作者：已核对的访谈作者/制作机构`、`摘要：“内容。”`、第一张图片排序；作者和摘要都在首图前，摘要末尾不署名。不要把嘉宾或摘要发言人误作访谈作者，不另列“原访谈：……”行。Z Highlights不套外层引号、引用块或来源引用。正式欢迎和告别照常保留。文末先写`原视频：完整英文原题`，下一非空段仅写原始URL，普通文字、不设超链接、不加其他标签。英文稿入口仍放编辑评论。

图片出处另存项目`qa/image-sources.json`，在验收证据中用`image_sources_file`指向实际文件。格式为`{"images": [{"shape_id": "实际图片docPr的id", "source_url": "具体原始出处链接"}]}`；覆盖封面和每张正文图。可补充本地图片路径及描述，便于回查；辅助资料不作为第四份交付稿。

## 豆包审查

运行前读取rules.json的`review_prompt`原文，并确认当前用户已授权向豆包发送本期全文。个人配置或安装Skill不授予上传权限。可通过已授权浏览器/连接访问豆包；不修改用户浏览器设置或网络配置，不安装下载插件，不索取密码，不绕过登录。请求用户登录是有效的未完成事项，不是已经审核。

提交内容：标题、摘要、Highlights、介绍、全部正文、图注及结尾；不发送原始双语素材、内部批注或无关隐私。提取Word文字时必须包含超链接文字及表格（若有），不能只用paragraph.text漏掉内容。

保存纯文本为`working/豆包提交全文.txt`、豆包回复为`qa/豆包审查回复.txt`或实际截图。记录提交全文的SHA256以及实际日期时间。超限分批时逐批记录覆盖的字符范围及回复，确认全文覆盖；不能拿一批结果代表全文。

无风险：中文成品末尾全文批注写rules.json中的`no_risk_comment`，同时注明“豆包审查”、审查时间、全文范围和提交全文SHA256，不把AI审查说成平台承诺。交付消息另告知豆包未识别出潜在风险。

有风险：每处风险给对应句段加Word批注，保留豆包实际原因和建议；同时记录评论ID/定位，避免只在全文末尾笼统说有风险。不自动删改；用户决定如何处理后对最终文本重审。

若全文正文改动，旧哈希与最终文本不匹配，审核视为过期。在旧审核批注末追加“已失效：正文已变更，待重新审核”，保留原结论作为历史，不隐藏或解决评论。重审完成后新增有时间及新SHA256的审核评论；受阻时不得让旧评论仍呈现有效结论。只添加批注不影响审查文本。失败时保留文件并明确注明未完成，不虚报验收通过。

## 检查证据

在qa目录保存`review-evidence.json`，以下是字段结构，值必须来自本期实际工作，不照抄测试数据：

```json
{
  "timestamps_available": true,
  "alignment_verified": true,
  "content_review_verified": true,
  "interview_credit": "已核对的访谈作者、节目或制作/发布机构",
  "original_title": "已核对的视频或播客完整英文标题",
  "original_url": "已核对的原视频/节目URL",
  "image_sources_file": "qa/image-sources.json的实际绝对路径",
  "experience_checks": {
    "transcript": {"status": "passed", "checked_ids": ["实际读取的条目ID"], "record_file": "qa/experience-checks.md的绝对路径"},
    "translation": {"status": "passed", "checked_ids": ["实际读取的条目ID"], "record_file": "实际自检记录绝对路径"},
    "packaging": {"status": "passed", "checked_ids": ["实际读取的条目ID"], "record_file": "实际自检记录绝对路径"},
    "images": {"status": "passed", "checked_ids": ["实际读取的条目ID"], "record_file": "实际自检记录绝对路径"},
    "review": {"status": "passed", "checked_ids": ["实际读取的条目ID"], "record_file": "实际自检记录绝对路径"},
    "delivery": {"status": "passed", "checked_ids": ["实际读取的条目ID"], "record_file": "实际自检记录绝对路径"}
  },
  "doubao": {
    "status": "no_risk",
    "reviewed_at": "实际审查的ISO日期时间",
    "prompt": "rules.json中的完整提示词",
    "text_sha256": "最终中文全文的实际SHA256",
    "response_files": ["实际保存的豆包返回文件绝对路径"]
  },
  "visual_review": {
    "english": {"reviewed": true, "docx_sha256": "实际文件哈希", "page_images": ["实际逐页PNG绝对路径"]},
    "bilingual": {"reviewed": true, "docx_sha256": "实际文件哈希", "page_images": ["实际逐页PNG绝对路径"]},
    "final": {"reviewed": true, "docx_sha256": "实际文件哈希", "page_images": ["实际逐页PNG绝对路径"]}
  }
}
```

status只能用`no_risk`、`risk_found`或`pending`；风险状态还应记录`comment_ids`。不能用自己写的结论文本假冒response_files。不曾逐页看过则reviewed为false。

六阶段经验自检只在确实读过对应清单并核对结果后记passed；待修问题记needs_fix，受阻记blocked。checked_ids记录本轮实际读取的ID，record_file包含结果及核对定位，不复制整份经验。部分任务不必执行无关阶段，但完整三稿的全流程验收要求六阶段均完成。阶段文件为空时用status=no_experience、checked_ids=[]并说明，不能把存在经验的阶段跳过。

检查器的`--extract-final path.txt`可导出用于审核的全文；`final_text_sha256`使用该算法：从DOCX的正文XML读取各段落的所有w:t（含超链接及表格段落），保留顺序，以换行连接非空段，UTF-8编码计算SHA256。不要手动改为另一套哈希算法。

检查脚本不改文件，JSON报告写qa目录；报告通过只表示检查条件成立，不证明翻译或豆包截图真实性，仍需人工/模型对照复核。核心句加粗10—20处、字体、完整句强调、真实空格和视觉缺陷需通过文字和渲染审查，不能伪称正则足以验证。

## 交付消息

分别给出三份Word文件，三个候选标题、原题译文、豆包实际结果和任何未完成事项。不要输出QA图、日志、脚本当成额外交付稿。不替用户导入飞书、发公众号或通知mentor。

本Skill是可调用流程，不是后台计划任务。不会自动登录豆包，不提供账号或字幕服务，不保证平台审查一定通过。遇阻完成能做部分，只集中询问必要信息。
