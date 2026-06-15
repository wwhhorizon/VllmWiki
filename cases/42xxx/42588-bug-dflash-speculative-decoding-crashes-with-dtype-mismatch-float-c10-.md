# vllm-project/vllm#42588: [Bug]: DFlash speculative decoding crashes with dtype mismatch: float != c10::Half in qwen3_dflash.py

| 字段 | 值 |
| --- | --- |
| Issue | [#42588](https://github.com/vllm-project/vllm/issues/42588) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DFlash speculative decoding crashes with dtype mismatch: float != c10::Half in qwen3_dflash.py

### Issue 正文摘录

### Your current environment **Environment:** - vLLM: 0.20.2 - ROCm: 6.4.2 - Hardware: AMD Strix Halo (gfx1151) - Model: Qwen3.6-27B-AWQ with z-lab/Qwen3.6-27B-DFlash drafter **Error:** RuntimeError: expected mat1 and mat2 to have the same dtype, but got: float != c10::Half Location: vllm/model_executor/models/qwen3_dflash.py line 588 Function: combine_hidden_states **Root cause:** On ROCm, hidden states are promoted to float32. The fc layer weights are float16. This causes dtype mismatch on matrix multiplication. **Fix:** Add one line before line 588: hidden_states = hidden_states.to(self.model.fc.weight.dtype) result = self.model.fc(hidden_states) **Note:** This does not occur on CUDA builds — ROCm specific. ### 🐛 Describe the bug RuntimeError: expected mat1 and mat2 to have the same dtype, but got: float != c10::Half File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/async_llm.py", line 660, in output_handler outputs = await engine_core.get_output_async() File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core_client.py", line 998, in get_output_async raise self._format_exception(outputs) from None vllm.v1.engine.exceptions.EngineDeadError: EngineCore encoun...

## 现有链接修复摘要

#43242 [Fix] fp32 residual dtype leak in GemmaRMSNorm.forward_native

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: speculative decoding crashes with dtype mismatch: float != c10::Half in qwen3_dflash.py bug;rocm ### Your current environment **Environment:** - vLLM: 0.20.2 - ROCm: 6.4.2 - Hardware: AMD Strix Halo (gfx1151) - Model: Q...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lt = self.model.fc(hidden_states) **Note:** This does not occur on CUDA builds — ROCm specific. ### 🐛 Describe the bug RuntimeError: expected mat1 and mat2 to have the same dtype, but got: float != c10::Half File "/usr/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: DFlash speculative decoding crashes with dtype mismatch: float != c10::Half in qwen3_dflash.py bug;rocm ### Your current environment **Environment:** - vLLM: 0.20.2 - ROCm: 6.4.2 - Hardware: AMD Strix Halo (gfx11...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: DFlash speculative decoding crashes with dtype mismatch: float != c10::Half in qwen3_dflash.py bug;rocm ### Your current environment **Environment:** - vLLM: 0.20.2 - ROCm: 6.4.2 - Hardware: AMD Strix Halo (gfx11...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: DFlash speculative decoding crashes with dtype mismatch: float != c10::Half in qwen3_dflash.py bug;rocm ### Your current environment **Environment:** - vLLM: 0.20.2 - ROCm: 6.4.2 - Hardware: AMD Strix Halo (gfx11...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43242](https://github.com/vllm-project/vllm/pull/43242) | closes_keyword | 0.95 | [Fix] fp32 residual dtype leak in GemmaRMSNorm.forward_native | Fixes issue #42588 GemmaRMSNorm.forward_native upcasts x+residual to fp32 for numerical stability but only casts the output back to orig_dtype, returning the residual in fp32. T |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
