# vllm-project/vllm#36718: [Bug]: vLLM 0.15.0 startup on H200 failed at deep_gemm

| 字段 | 值 |
| --- | --- |
| Issue | [#36718](https://github.com/vllm-project/vllm/issues/36718) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;quantization |
| 子分类 | cold_start |
| Operator 关键词 | fp8;gemm;kernel |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.15.0 startup on H200 failed at deep_gemm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` 0.15.1 4:57:02 PM [algo-1-1772841836] [vllm.server] Traceback (most recent call last): 4:57:02 PM [algo-1-1772841836] [vllm.server] RuntimeError: Worker failed with error 'Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0', please check the stack trace above for the root cause 4:57:03 PM [algo-1-1772841836] [vllm.server] Traceback (most recent call last): 4:57:03 PM [algo-1-1772841836] [vllm.server] RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} 4:57:10 PM [algo-1-1772841836] [VLLM_STATUS] ✗ Configuration failed: VLLM: DP=1, TP=8, KV=0.7, eager 4:57:10 PM [algo-1-1772841836] [VLLM_STATUS] ✗ All vLLM configurations failed 4:57:10 PM [algo-1-1772841836] /opt/wrapper/libfarm/lib/python3.11/site-packages/watchtower/__init__.py:464: WatchtowerWarning: Received message after logging system shutdown warnings.warn("Received message after logging system shutdown", WatchtowerWarning) 4:57:10 PM [algo-1-1772841836] [VLLM_STATUS] Stopping server server (PID: 68574) ``` ### Before submitting a new issue... - [x] Make sure you already searched fo...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ked questions. performance distributed_parallel;frontend_api;gemm_linear;quantization fp8;gemm;kernel crash dtype Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: . Failed core proc(s): {} 4:57:10 PM [algo-1-1772841836] [VLLM_STATUS] ✗ Configuration failed: VLLM: DP=1, TP=8, KV=0.7, eager 4:57:10 PM [algo-1-1772841836] [VLLM_STATUS] ✗ All vLLM configurations failed 4:57:10 PM [al...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: vLLM 0.15.0 startup on H200 failed at deep_gemm bug ### Your current environment ### 🐛 Describe the bug ``` 0.15.1 4:57:02 PM [algo-1-1772841836] [vllm.server] Traceback (most recent call last): 4:57:02 PM [algo-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;frontend_api;gemm_linear;quantization fp8;gemm;kerne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
