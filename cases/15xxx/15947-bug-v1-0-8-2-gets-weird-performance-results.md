# vllm-project/vllm#15947: [Bug]: v1 0.8.2 gets weird performance results

| 字段 | 值 |
| --- | --- |
| Issue | [#15947](https://github.com/vllm-project/vllm/issues/15947) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v1 0.8.2 gets weird performance results

### Issue 正文摘录

### Your current environment I used random data to call the completions interface and compared vllm v1 v0.7.3 and v0.8.2 on A100 using Qwen2.5-7B-Instruct and found that the results of v0.8.2 were very strange. The service startup command is: `VLLM_USE_V1="1" vllm serve {model_path} --trust-remote-code --gpu-memory-utilization 0.9 --port 8000 --dtype bfloat16 --served-model-name Qwen2.5-7B-Instruct --disable-custom-all-reduce --tensor-parallel-size 1` ## Input32 output 2048 ![Image](https://github.com/user-attachments/assets/147e19a6-d6d3-4f26-983d-b99357d2f5ce) ## input512 output1024 ![Image](https://github.com/user-attachments/assets/99bddc59-595b-4da4-8200-798014464fca) ## input1024 output512 ![Image](https://github.com/user-attachments/assets/dcd27f8e-90ed-4507-a955-211b13e6d5aa) ## input2048 output512 ![Image](https://github.com/user-attachments/assets/cc6da3a9-adcc-496f-960e-234b9f7ace9f) ## input4096 output1024 ![Image](https://github.com/user-attachments/assets/85d849ff-3171-438c-974a-e6adf266ca43) ## input16000 output4000 ![Image](https://github.com/user-attachments/assets/c6d28c7d-1f13-4ff3-8d02-e7fcdb46e685) ### 🐛 Describe the bug ![Image](https://github.com/user-attach...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: del_path} --trust-remote-code --gpu-memory-utilization 0.9 --port 8000 --dtype bfloat16 --served-model-name Qwen2.5-7B-Instruct --disable-custom-all-reduce --tensor-parallel-size 1` ## Input32 output 2048 ![Image](https...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: call the completions interface and compared vllm v1 v0.7.3 and v0.8.2 on A100 using Qwen2.5-7B-Instruct and found that the results of v0.8.2 were very strange. The service startup command is: `VLLM_USE_V1="1" vllm serve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mpletions interface and compared vllm v1 v0.7.3 and v0.8.2 on A100 using Qwen2.5-7B-Instruct and found that the results of v0.8.2 were very strange. The service startup command is: `VLLM_USE_V1="1" vllm serve {model_pat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: v1 0.8.2 gets weird performance results bug;stale ### Your current environment I used random data to call the completions interface and compared vllm v1 v0.7.3 and v0.8.2 on A100 using Qwen2.5-7B-Instruct and fou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
