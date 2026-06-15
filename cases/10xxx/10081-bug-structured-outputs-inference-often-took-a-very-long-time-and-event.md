# vllm-project/vllm#10081: [Bug]:Structured outputs inference often took a very long time,and eventually causing a timeout and vLLM engine crushing.

| 字段 | 值 |
| --- | --- |
| Issue | [#10081](https://github.com/vllm-project/vllm/issues/10081) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Structured outputs inference often took a very long time,and eventually causing a timeout and vLLM engine crushing.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Structured output inference can take a very long time, even with just a single request, ultimately leading to timeouts or crashes. During inference, GPU KV cache usage gradually increases to 100%, while the average generation throughput drops from 30 tokens/s to 20 tokens/s, eventually causing a timeout and necessitating the use of the CPU KV cache. Even after one hour, there is no response to the structured output request sent earlier. Subsequently, I sent additional requests, including both normal and structured ones; the normal requests were responded to, albeit slowly, while the structured requests received no response. Over several more hours, an increasing number of new requests became pending and sequences were swapped, which eventually led to the vLLM engine crashing. However, everything operates smoothly when only normal chat completion requests are sent, achieving an average generation throughput of 100 tokens/s or higher on dual Tesla V100 GPUs. The test model used was Qwen2-32B-GPTQ-Int8. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda;quantizatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ventually led to the vLLM engine crashing. However, everything operates smoothly when only normal chat completion requests are sent, achieving an average generation throughput of 100 tokens/s or higher on dual Tesla V10...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tually causing a timeout and vLLM engine crushing. bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Structured output inference can take a very long tim...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda;quantization;sampling;triton build_error;crash;nan_inf;slowdown dtype;env_dependency...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ushing. bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Structured output inference can take a very long time, even with just a single request, ultimat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
