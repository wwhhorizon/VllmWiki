# vllm-project/vllm#12427: [Bug]: macOS with vllm-cpu v0.6.6-post2 serving Qwen2.5-1.5b-Instruct results in endless exclamation marks

| 字段 | 值 |
| --- | --- |
| Issue | [#12427](https://github.com/vllm-project/vllm/issues/12427) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: macOS with vllm-cpu v0.6.6-post2 serving Qwen2.5-1.5b-Instruct results in endless exclamation marks

### Issue 正文摘录

### Your current environment OS: Apple M2 Max, mem 96G, macOS Sonoma 14.5 Python: 3.12.8 transformers 4.48.1 torch 2.5.1 vllm 0.6.6.post2.dev378+g324960a9.cpu Followed instructions on https://docs.vllm.ai/en/latest/getting_started/installation/cpu/index.html to setup env for macOS Have checked every issue refering to the endless exclamation problem, but with 0.6.6 & macOS I believe this is new situation. ### Model Input Dumps _No response_ ### 🐛 Describe the bug MacOS 用vllm-cpu v0.6.6从原版到post1、post2均有 Qwen2.5-1.5b-Instruct、Deepseek-R1-Qwen-1.5b输出均为重复感叹号的问题，Qwen2.5-0.5b-Instruct无问题。 Setup in conda env, serving without using docker Can get normal results with Qwen2.5-0.5b-Instruct & Qwen1.5-1.8b-Instruct. But can only get endless exclamations when using Qwen2.5-1.5b-Instruct or Deepseek-R1-Qwen-1.5b. Expect Qwen2.5-1.5B-Instruct & Deepseek-R1-Qwen-1.5b to have normal output. Have tried transformer infer with these 2 models, and got normal results. Serving Code: ``` bash export VLLM_TARGET_DEVICE=cpu export VLLM_CPU_KVCACHE_SPACE=8 python3 -m vllm.entrypoints.openai.api_server \ --model /Users/xxx/mac_vllm/hfmodels/model_qwen_qwen1.5-1.8b-chat \ --served-model-name Qwen1.5-1.8B-Chat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Followed instructions on https://docs.vllm.ai/en/latest/getting_started/installation/cpu/index.html to setup env for macOS Have checked every issue refering to the endless exclamation problem, but with 0.6.6 & macOS I b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: macOS with vllm-cpu v0.6.6-post2 serving Qwen2.5-1.5b-Instruct results in endless exclamation marks bug;stale ### Your current environment OS: Apple M2 Max, mem 96G, macOS Sonoma 14.5 Python:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: % ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: d-model-name Qwen1.5-1.8B-Chat \ --trust-remote-code \ --dtype=half \ --host 0.0.0.0 \ --port 30000 python3 -m vllm.entrypoints.openai.api_server \ --model /Users/xxx/mac_vllm/hfmodels/model_qwen_qwen2.5-0.5b-instruct \...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ": "user", "content": "你好，可以帮我写一个小说开头吗？"} ], "stream": false, "max_tokens": 100 }' ``` {"id":"cmpl-b5d774d8ca6843e2971c89b64fd60c8f","object":"text_completion","created":1737812909,"model":"Qwen1.5-1.8B-Chat","choices":...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
