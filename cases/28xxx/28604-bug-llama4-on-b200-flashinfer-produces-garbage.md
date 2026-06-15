# vllm-project/vllm#28604: [Bug]: Llama4 on B200 flashinfer produces garbage

| 字段 | 值 |
| --- | --- |
| Issue | [#28604](https://github.com/vllm-project/vllm/issues/28604) |
| 状态 | closed |
| 标签 | bug;torch.compile;nvidia |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Llama4 on B200 flashinfer produces garbage

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug test_fusions_e2e.py::test_attn_quant is broken for llama4. Issue can be reproduced with the following simple command: ``` # no fusion also broken python examples/offline_inference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --kv-cache-dtype=fp8 --max-model-len=1024 # original repro python examples/offline_inference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --kv-cache-dtype=fp8 --max-model-len=1024 -O.enable_noop=true -O.enable_attn_fusion=true -O.use_inductor_partition=true # works VLLM_ATTENTION_BACKEND=TRITON_ATTN python examples/offline_inference/basic/generate.py --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --kv-cache-dtype=fp8 --max-model-len=1024 -O.enable_noop=true -O.enable_attn_fusion=true -O.use_inductor_partition=true ``` Outputs: ``` -------------------------------------------------- Prompt: 'Hello, my name is' Generated text: ' Christine and; 디지털을 that. new2ed micbedd: 왔으니\n pack' -------------------------------------------------- Prompt: 'The president of the United States is' Generated text: ' the дме,,,,5ccfed rightmostdd* wr ~ Raff' --------------------------...

## 现有链接修复摘要

#27126 [compile] Enable sequence parallelism matching w/o custom ops enabled | #28739 [Bugfix] Fix ChunkedLocalAttention CUDA Graph setting | #28966 Re-enable FlashInfer for Llama4 on Blackwell in e2e fusion tests

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Llama4 on B200 flashinfer produces garbage bug;torch.compile;nvidia ### Your current environment ### 🐛 Describe the bug test_fusions_e2e.py::test_attn_quant is broken for llama4. Issue can be reproduced with the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Llama4 on B200 flashinfer produces garbage bug;torch.compile;nvidia ### Your current environment ### 🐛 Describe the bug test_fusions_e2e.py::test_attn_quant is broken for llama4. Issue can be reproduced with the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama4 on B200 flashinfer produces garbage bug;torch.compile;nvidia ### Your current environment ### 🐛 Describe the bug test_fusions_e2e.py::test_attn_quant is broken for llama4. Issue can be reproduced with the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Llama4 on B200 flashinfer produces garbage bug;torch.compile;nvidia ### Your current environment ### 🐛 Describe the bug test_fusions_e2e.py::test_attn_quant is broken for llama4. Issue can be reproduced with the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: t environment ### 🐛 Describe the bug test_fusions_e2e.py::test_attn_quant is broken for llama4. Issue can be reproduced with the following simple command: ``` # no fusion also broken python examples/offline_inference/ba...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27126](https://github.com/vllm-project/vllm/pull/27126) | mentioned | 0.45 | [compile] Enable sequence parallelism matching w/o custom ops enabled  | -------- ``` the test also sometimes produces an ima - it happens on #27126 but not on main, not sure why. <details> <summary>full logs</summary> ``` info 11-12 19:56:47 [utils.py… |
| [#28739](https://github.com/vllm-project/vllm/pull/28739) | closes_keyword | 0.95 | [Bugfix] Fix ChunkedLocalAttention CUDA Graph setting | FIX #28604 |
| [#28966](https://github.com/vllm-project/vllm/pull/28966) | mentioned | 0.6 | Re-enable FlashInfer for Llama4 on Blackwell in e2e fusion tests | nal FlashInfer on Blackwell, TRITON_ATTN otherwise - Removed TODO and #28604 reference (fixed) - Changed Llama3 to use TRITON_ATTN consistently (removed conditional backend logic)… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
