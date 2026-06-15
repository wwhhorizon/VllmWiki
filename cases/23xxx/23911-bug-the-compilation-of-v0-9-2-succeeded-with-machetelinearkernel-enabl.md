# vllm-project/vllm#23911: [Bug]: The compilation of v0.9.2 succeeded with MacheteLinearKernel enabled for the RTX 4090 (CUDA architecture 8.9), but a runtime error was encountered.

| 字段 | 值 |
| --- | --- |
| Issue | [#23911](https://github.com/vllm-project/vllm/issues/23911) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The compilation of v0.9.2 succeeded with MacheteLinearKernel enabled for the RTX 4090 (CUDA architecture 8.9), but a runtime error was encountered.

### Issue 正文摘录

### Your current environment RTX4090 GPU nvidia driver 550/560/570 ubuntu 2204/2404 cuda 12.4/12.6/12.8 torch 2.6/2.7 python 3.12 vllm 9.2rc2 All these envs are the same. following bugs are under 560, 2204,12.6, 2.7, 3.12, 9.2rc2 The same bugs will **NOT** encounter in 5080 envs. ### 🐛 Describe the bug When run a dense model, is OK. When run a MoE GPTQ/AWQ model. **I think is because MacheteLinearKernel is not support 4090 arch 89 , but, how can I config to another kernel??** BUGS details: **DeepSeek-V2-Lite-gptq-4bit/Qwen3-30B-A3B-GPTQ-Int4** gptq_marlin: ``` INFO 08-29 09:19:41 [gptq_marlin.py:266] Using MarlinLinearKernel for GPTQMarlinLinearMethod INFO 08-29 09:19:41 [cuda.py:208] Using Triton MLA backend on V1 engine. ERROR 08-29 09:19:41 [core.py:586] EngineCore failed to start. ERROR 08-29 09:19:41 [core.py:586] Traceback (most recent call last): ERROR 08-29 09:19:41 [core.py:586] File "/home/Develop/vllm/vllm/v1/engine/core.py", line 577, in run_engine_core ERROR 08-29 09:19:41 [core.py:586] engine_core = EngineCoreProc(*args, **kwargs) ERROR 08-29 09:19:41 [core.py:586] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-29 09:19:41 [core.py:586] File "/home/Develop/vllm/vllm/v1/eng...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: compilation of v0.9.2 succeeded with MacheteLinearKernel enabled for the RTX 4090 (CUDA architecture 8.9), but a runtime error was encountered. bug;stale ### Your current environment RTX4090 GPU nvidia driver 550/560/57...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: me/Develop/vllm/vllm/model_executor/layers/quantization/kernels/mixed_precision/__init__.py", line 80, in choose_mp_linear_kernel ERROR 08-29 09:19:41 [core.py:586] raise ValueError( ERROR 08-29 09:19:41 [core.py:586] V...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ernel??** BUGS details: **DeepSeek-V2-Lite-gptq-4bit/Qwen3-30B-A3B-GPTQ-Int4** gptq_marlin: ``` INFO 08-29 09:19:41 [gptq_marlin.py:266] Using MarlinLinearKernel for GPTQMarlinLinearMethod INFO 08-29 09:19:41 [cuda.py:2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: *NOT** encounter in 5080 envs. ### 🐛 Describe the bug When run a dense model, is OK. When run a MoE GPTQ/AWQ model. **I think is because MacheteLinearKernel is not support 4090 arch 89 , but, how can I config to another...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ernel for GPTQMarlinLinearMethod INFO 08-29 09:19:41 [cuda.py:208] Using Triton MLA backend on V1 engine. ERROR 08-29 09:19:41 [core.py:586] EngineCore failed to start. ERROR 08-29 09:19:41 [core.py:586] Traceback (most...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | In: body) • gfx (substring) in body: 7 matches (searchIn: both) #23911: Should have ROCm label: NO (0 matches) #23910: Should have ROCm label: NO (0 matches) #23905: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
