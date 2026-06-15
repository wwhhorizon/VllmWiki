# vllm-project/vllm#18396: [Bug]: After setting VLLM_TARGET_DEVICE=cpu, compilation failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#18396](https://github.com/vllm-project/vllm/issues/18396) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After setting VLLM_TARGET_DEVICE=cpu, compilation failed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After I run the command: `VLLM_TARGET_DEVICE=cpu python setup.py install` Got the error: ``` configuration error: `project.license` must be valid exactly by one definition (2 matches found): - keys: 'file': {type: string} required: ['file'] - keys: 'text': {type: string} required: ['text'] DESCRIPTION: `Project license `_. GIVEN VALUE: "Apache-2.0" OFFENDING RULE: 'oneOf' DEFINITION: { "oneOf": [ { "properties": { "file": { "type": "string", "$$description": [ "Relative path to the file (UTF-8) which contains the license for the", "project." ] } }, "required": [ "file" ] }, { "properties": { "text": { "type": "string", "$$description": [ "The license of the project whose meaning is that of the", "`License field from the core metadata", " `_." ] } }, "required": [ "text" ] } ] } Traceback (most recent call last): File "/workspace/vllm_source/setup.py", line 688, in setup( File "/usr/local/lib/python3.10/dist-packages/setuptools/__init__.py", line 103, in setup return distutils.core.setup(**attrs) File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/core.py", line 159, in setup dist.parse_config_files() File "/usr/lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: he bug After I run the command: `VLLM_TARGET_DEVICE=cpu python setup.py install` Got the error: ``` configuration error: `project.license` must be valid exactly by one definition (2 matches found): - keys: 'file': {type...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lly ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: and: `VLLM_TARGET_DEVICE=cpu python setup.py install` Got the error: ``` configuration error: `project.license` must be valid exactly by one definition (2 matches found): - keys: 'file': {type: string} required: ['file'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;import_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: that of the", "`License field from the core metadata", " `_." ] } }, "required": [ "text" ] } ]

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
