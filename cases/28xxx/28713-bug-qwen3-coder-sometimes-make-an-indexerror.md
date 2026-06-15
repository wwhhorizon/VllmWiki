# vllm-project/vllm#28713: [Bug]: qwen3-coder sometimes make an IndexError

| 字段 | 值 |
| --- | --- |
| Issue | [#28713](https://github.com/vllm-project/vllm/issues/28713) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen3-coder sometimes make an IndexError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Start with: ``` vllm serve /models/Qwen3-Coder-30B-A3B-Instruct/ --served-model-name qwen3-coder-30b-a3b-instruct --port 40410 --max-model-len 128000 --enable-expert-parallel --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser qwen3_coder ``` Http request: [request.txt](https://github.com/user-attachments/files/23541996/request.txt) Sometimes, there will be a IndexError when the final output is a batch of tokens. I add some logs which start with "=====", and it shows the `tool_parser.streamed_args_for_tool` is always empty. Is that a problem? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling buil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: qwen3-coder sometimes make an IndexError bug;stale ### Your current environment ### 🐛 Describe the bug Start with: ``` vllm serve /models/Qwen3-Coder-30B-A3B-Instruct/ --served-model-name qwen3-coder-30b-a3b-inst...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3-coder sometimes make an IndexError bug;stale ### Your current environment ### 🐛 Describe the bug Start with: ``` vllm serve /models/Qwen3-Coder-30B-A3B-Instruct/ --served-model-name qwen3-coder-30b-a3b-inst...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: wen3-coder-30b-a3b-instruct --port 40410 --max-model-len 128000 --enable-expert-parallel --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser qwen3_coder ``` Http request: [request.txt](https://github.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
