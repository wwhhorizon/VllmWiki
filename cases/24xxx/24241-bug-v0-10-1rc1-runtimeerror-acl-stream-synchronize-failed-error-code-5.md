# vllm-project/vllm#24241: [Bug]: v0.10.1rc1 推理偶现RuntimeError: ACL stream synchronize failed, error code:507035

| 字段 | 值 |
| --- | --- |
| Issue | [#24241](https://github.com/vllm-project/vllm/issues/24241) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.10.1rc1 推理偶现RuntimeError: ACL stream synchronize failed, error code:507035

### Issue 正文摘录

### Your current environment 昇腾910B3 4卡推理Qwen3-Coder-30B-A3B-Instruct ### 🐛 Describe the bug [rank0]:[W904 09:50:12.024496247 compiler_depend.ts:57] Warning: EZ9999: Inner Error! EZ9999: [PID: 838] 2025-09-04-09:50:11.954.378 The error from device(chipId:6, dieId:0), serial number is 8, there is an exception of aivec error, core id is 40, error code = 0, dump info: pc start: 0x124101423000, current: 0x12410142395c, vec error info: 0x6b07d2ab62, mte error info: 0xf3060000e6, ifu error info: 0x20003fffeda00, ccu error info: 0x8f01200800000000, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x124140505400.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303] TraceBack (most recent call last): The extend info: errcode:(0, 0x8000, 0) errorStr: When the D-cache reads and writes data to the UB, the response value returned by the bus is a non-zero value. fixp_error0 info: 0x60000e6, fixp_error1 info: 0xf3, fsmId:1, tslot:0, thread:0, ctxid:0, blk:3, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322] Kernel task happen error, retCode=0x31, [vector core exception].[FUNC:PreCheckTaskErr][...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [multiproc_executor.py:596] output = self.model_runner.execute_model(scheduler_output, (VllmWorker TP0 pid=838) ERROR 09-04 09:50:12 [multiproc_executor.py:596] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rride_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: r! EZ9999: [PID: 838] 2025-09-04-09:50:11.954.378 The error from device(chipId:6, dieId:0), serial number is 8, there is an exception of aivec error, core id is 40, error code = 0, dump info: pc start: 0x124101423000, c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ro value. fixp_error0 info: 0x60000e6, fixp_error1 info: 0xf3, fsmId:1, tslot:0, thread:0, ctxid:0, blk:3, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322] Kernel task hap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: failed, error code:507035 bug ### Your current environment 昇腾910B3 4卡推理Qwen3-Coder-30B-A3B-Instruct ### 🐛 Describe the bug [rank0]:[W904 09:50:12.024496247 compiler_depend.ts:57] Warning: EZ9999: Inner Error! EZ9999: [P...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
