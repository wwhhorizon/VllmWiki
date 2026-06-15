# vllm-project/vllm#14025: [Bug]: Waiting for output from MQLLMEngine. Hangs and then crashes after about an 1 hour

| 字段 | 值 |
| --- | --- |
| Issue | [#14025](https://github.com/vllm-project/vllm/issues/14025) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Waiting for output from MQLLMEngine. Hangs and then crashes after about an 1 hour

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM deployed on a k8s/opernshift cluster hangs and crashes. Testing on 4 L40s GPUs with LLama 8B so I know the model should fit. For debugging, installed Model on local disk before running VLLM I ran the following test.py and it hangs after PyTorch NCCL is successful! [Full Description](https://gist.github.com/jayteaftw/6e4844fc64cca3e78f63e2c6d10b6083) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 4 L40s GPUs with LLama 8B so I know the model should fit. For debugging, installed Model on local disk before running VLLM I ran the following test.py and it hangs after PyTorch NCCL is successful! [Full Description](ht...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Waiting for output from MQLLMEngine. Hangs and then crashes after about an 1 hour bug;stale ### Your current environment ### 🐛 Describe the bug VLLM deployed on a k8s/opernshift cluster hangs and crashes. Testing...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 83) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a k8s/opernshift cluster hangs and crashes. Testing on 4 L40s GPUs with LLama 8B so I know the model should fit. For debugging, installed Model on local disk before running VLLM I ran the following test.py and it hangs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
