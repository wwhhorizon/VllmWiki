# vllm-project/vllm#11686: [Bug]: vLLM is erroneously sending some information outputs into the error stream

| 字段 | 值 |
| --- | --- |
| Issue | [#11686](https://github.com/vllm-project/vllm/issues/11686) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM is erroneously sending some information outputs into the error stream

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![image](https://github.com/user-attachments/assets/a8bc2180-37a3-49f2-a3e6-0b6185846d38) ![image](https://github.com/user-attachments/assets/d93422a8-1da1-40d6-b96b-b75a2db65447) In order to benchmarking of vLLM servers I am doing output redirection and parsing the output so I can tell when the server is ready to accept inference requests. It turns out, it is outputting parts of the output into the error stream for whatever reason. This tripped me up. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s erroneously sending some information outputs into the error stream bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![image](https://github.com/user-attachments/assets/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: up. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM is erroneously sending some information outputs into the error stream bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![image](https://github.com/user-attach...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ser-attachments/assets/d93422a8-1da1-40d6-b96b-b75a2db65447) In order to benchmarking of vLLM servers I am doing output redirection and parsing the output so I can tell when the server is ready to accept inference reque...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
