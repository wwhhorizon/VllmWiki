# vllm-project/vllm#8933: [Bug]: Vllm0.6.2 UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown

| 字段 | 值 |
| --- | --- |
| Issue | [#8933](https://github.com/vllm-project/vllm/issues/8933) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Vllm0.6.2 UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug (demo_vllm) demo@dgx03:/raid/xinference/modelscope/hub/qwen/Qwen2-72B-Instruct/logs$ tail -f vllm_20240927.log frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x57 (0x7f5cf7ba9897 in /raid/demo/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/lib/libc10.so) frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional > >) + 0x1d2 (0x7f5cf8e82c62 in /raid/demo/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1a0 (0x7f5cf8e87a80 in /raid/demo/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10c (0x7f5cf8e88dcc in /raid/demo/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #4: + 0xdbbf4 (0x7f5d44931bf4 in /raid/demo/anaconda3/envs/vllm/bin/../lib/libstdc++.so.6) frame #5: + 0x8609 (0x7f5d4618b609 in /lib/x86_64-linux-gnu/libpthread.so.0) frame #6: clone + 0x43 (0x7f5d45f56353 in /lib/x86_64-linux-gnu/libc.so.6) /raid/demo/anaconda3/envs/vllm/lib/python3.10/multiproce...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: demo/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1a0 (0x7f5cf8e87a80 in /raid/demo/anaconda3/envs/vllm/lib/python3.10/site-package...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: objects to clean up at shutdown bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug (demo_vllm) demo@dgx03:/raid/xinference/modelscope/hub/qwen/Qwen2-72B-Instruct/logs$ tail -f vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
