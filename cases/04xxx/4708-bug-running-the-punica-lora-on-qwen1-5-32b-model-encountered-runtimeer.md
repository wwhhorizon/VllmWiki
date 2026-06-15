# vllm-project/vllm#4708: [Bug]: Running the punica lora on Qwen1.5 32B model encountered RuntimeError: No suitable kernel. h_in=64 h_out=3424 dtype=Float out_dtype=BFloat16

| 字段 | 值 |
| --- | --- |
| Issue | [#4708](https://github.com/vllm-project/vllm/issues/4708) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Running the punica lora on Qwen1.5 32B model encountered RuntimeError: No suitable kernel. h_in=64 h_out=3424 dtype=Float out_dtype=BFloat16

### Issue 正文摘录

### Your current environment 3090 8 gpus vllm 0.4.1 ### 🐛 Describe the bug Hello vllm team, When I try to run qwen1.5 32B model with punica lora request with tensor parallel size = 8, I have encountered the following error: punica_kernels.dispatch_bgmv_low_level( (RayWorkerWrapper pid=1566630) ERROR 04-26 16:28:41 worker_base.py:157] RuntimeError: No suitable kernel. h_in=64 h_out=3424 dtype=Float out_dtype=BFloat16 I am using 3090 machine with 8 gpus and I wish to use all my gpus. Can you have any chance to take look at this issue I am facing? Thank you very much!

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: B model encountered RuntimeError: No suitable kernel. h_in=64 h_out=3424 dtype=Float out_dtype=BFloat16 bug ### Your current environment 3090 8 gpus vllm 0.4.1 ### 🐛 Describe the bug Hello vllm team, When I try to run q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Running the punica lora on Qwen1.5 32B model encountered RuntimeError: No suitable kernel. h_in=64 h_out=3424 dtype=Float out_dtype=BFloat16 bug ### Your current environment 3090 8 gpus vllm 0.4.1 ### 🐛 Describe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel size = 8, I have encountered the following error: punica_kernels.dispatch_bgmv_low_level( (RayWorkerWrapper pid=1566630) ERROR 04-26 16:28:41 worker_base.py:157] RuntimeError: No suitable kernel. h_in=64 h_out=34...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e all my gpus. Can you have any chance to take look at this issue I am facing? Thank you very much!
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Hello vllm team, When I try to run qwen1.5 32B model with punica lora request with tensor parallel size = 8, I have encountered the following error: punica_kernels.dispatch_bgmv_low_level( (RayWorkerWrapper pid=1566630)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
