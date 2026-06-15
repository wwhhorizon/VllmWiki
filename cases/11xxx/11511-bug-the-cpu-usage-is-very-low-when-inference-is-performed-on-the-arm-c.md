# vllm-project/vllm#11511: [Bug]: The CPU usage is very low when inference is performed on the ARM CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#11511](https://github.com/vllm-project/vllm/issues/11511) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The CPU usage is very low when inference is performed on the ARM CPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I executed "VLLM_CPU_OMP_THREADS_BIND="0-39" taskset -c 0-39 python benchmark_throughput.py --input-len 256 --output-len 256 --num-prompts 10" to test the speed of decoding, the CPU usage was very low. The model used is Qwen2-1.5B-Instruct. ![ScreenShot_20241226171543](https://github.com/user-attachments/assets/e13ccfcd-ea74-44a2-a8d5-d1aa3c97e093) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: hen I executed "VLLM_CPU_OMP_THREADS_BIND="0-39" taskset -c 0-39 python benchmark_throughput.py --input-len 256 --output-len 256 --num-prompts 10" to test the speed of decoding, the CPU usage was very low. The model use...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: performed on the ARM CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I executed "VLLM_CPU_OMP_THREADS_BIND="0-39" taskset -c 0-39 python benchmark_throughput.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 93) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: The CPU usage is very low when inference is performed on the ARM CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I executed "VLLM_CPU_OMP_THREADS_BIND="0-39" ta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
