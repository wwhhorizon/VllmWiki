# vllm-project/vllm#16409: [Usage]: xpxd is useless？

| 字段 | 值 |
| --- | --- |
| Issue | [#16409](https://github.com/vllm-project/vllm/issues/16409) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: xpxd is useless？

### Issue 正文摘录

### Your current environment I am currently testing xpxd and found that the performance has not improved. Is there a problem of incorrect usage? Testing Machine：h100x80GBx8 vllm version：0.8.3 test model：DeepSeek-Coder-V2-Lite 1p1d separation test results： ![Image](https://github.com/user-attachments/assets/9dbba760-d09b-45c1-93f5-4ab6723f21e5) PD non-separation test results： ![Image](https://github.com/user-attachments/assets/f258df12-73e9-4178-8c5a-42dd85471e04) PD separation test method： ``` # 1p CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve \ /work/DeepSeek-Coder-V2-Lite-Instruct \ --served-model-name DeepSeek-Coder-V2-Lite \ --gpu-memory-utilization 0.8 \ --tensor-parallel-size 4 \ --trust-remote-code \ --enable-chunked-prefill \ --disable-log-requests \ --port 8100 # 1d CUDA_VISIBLE_DEVICES=4,5,6,7 vllm serve \ /work/DeepSeek-Coder-V2-Lite-Instruct \ --served-model-name DeepSeek-Coder-V2-Lite \ --gpu-memory-utilization 0.8 \ --tensor-parallel-size 4 \ --trust-remote-code \ --enable-chunked-prefill \ --disable-log-requests \ --port 8200 # proxy python3 examples/online_serving/disagg_examples/disagg_proxy_demo.py \ --model DeepSeek-Coder-V2-Lite \ --prefill localhost:8100 \ --decode...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: xpxd is useless？ usage;stale ### Your current environment I am currently testing xpxd and found that the performance has not improved. Is there a problem of incorrect usage? Testing Machine：h100x80GBx8 vllm ver...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Is there a problem of incorrect usage? Testing Machine：h100x80GBx8 vllm version：0.8.3 test model：DeepSeek-Coder-V2-Lite 1p1d separation test results： ![Image](https://github.com/user-attachments/assets/9dbba760-d09b-45c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: as not improved. Is there a problem of incorrect usage? Testing Machine：h100x80GBx8 vllm version：0.8.3 test model：DeepSeek-Coder-V2-Lite 1p1d separation test results： ![Image](https://github.com/user-attachments/assets/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: of incorrect usage? Testing Machine：h100x80GBx8 vllm version：0.8.3 test model：DeepSeek-Coder-V2-Lite 1p1d separation test results： ![Image](https://github.com/user-attachments/assets/9dbba760-d09b-45c1-93f5-4ab6723f21e5...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: pxd is useless？ usage;stale ### Your current environment I am currently testing xpxd and found that the performance has not improved. Is there a problem of incorrect usage? Testing Machine：h100x80GBx8 vllm version：0.8.3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
