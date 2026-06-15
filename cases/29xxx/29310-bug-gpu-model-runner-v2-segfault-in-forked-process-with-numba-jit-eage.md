# vllm-project/vllm#29310: [Bug][GPU Model Runner v2] Segfault in forked process with @numba.jit() eager compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#29310](https://github.com/vllm-project/vllm/issues/29310) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][GPU Model Runner v2] Segfault in forked process with @numba.jit() eager compilation

### Issue 正文摘录

### Your current environment commit 4de87866a8fdc9395ccd40e00c0f9075439b07ae ### 🐛 Describe the bug I haven't dug into this, early findings: ``` $> VLLM_USE_V2_MODEL_RUNNER=1 pytest -vs tests/v1/shutdown/test_delete.py::test_async_llm_delete[True-2-hmellor/tiny-random-LlamaForCausalLM] ... (EngineCore_DP0 pid=3138099) INFO 11-24 07:19:49 [distributed/parallel_state.py:1425] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 0, EP rank 0 (EngineCore_DP0 pid=3138099) INFO 11-24 07:19:49 [distributed/parallel_state.py:1425] rank 1 in world size 2 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 1, EP rank 1 Fatal Python error: Segmentation fault ... Current thread 0x00007f5442d0f740 (most recent call first): File "/home/markmc/vllm-project/vllm-venv/lib64/python3.12/site-packages/llvmlite/binding/ffi.py", line 197 in __call__ ... File "/home/markmc/vllm-project/vllm-venv/lib64/python3.12/site-packages/numba/core/dispatcher.py", line 885 in compile File "/home/markmc/vllm-project/vllm-venv/lib64/python3.12/site-packages/numba/core/decorators.py", line 232 in wrapper File "/home/markmc/vllm-project/vllm/vllm/v1/worker/gpu/input_batch.py", line 149 i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nv/lib64/python3.12/site-packages/numba/core/dispatcher.py", line 885 in compile File "/home/markmc/vllm-project/vllm-venv/lib64/python3.12/site-packages/numba/core/decorators.py", line 232 in wrapper File "/home/markmc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 149 in ... File "/home/markmc/vllm-project/vllm/vllm/v1/worker/gpu/cudagraph_utils.py", line 19 in ... File "/home/markmc/vllm-project/vllm/vllm/v1/worker/gpu/model_runner.py", line 37 in ... File "/home/markmc/vllm-pro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug][GPU Model Runner v2] Segfault in forked process with @numba.jit() eager compilation bug ### Your current environment commit 4de87866a8fdc9395ccd40e00c0f9075439b07ae ### 🐛 Describe the bug I haven't dug into this,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /markmc/vllm-project/vllm-venv/lib64/python3.12/site-packages/numba/core/dispatcher.py", line 885 in compile File "/home/markmc/vllm-project/vllm-venv/lib64/python3.12/site-packages/numba/core/decorators.py", line 232 i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ork * https://stackoverflow.com/questions/44764520/weird-multiprocessing-block-importing-numba-function: "Segfaults appearing from concurrent operations inside LLVM" and "issues with installing functions during Numba's...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
