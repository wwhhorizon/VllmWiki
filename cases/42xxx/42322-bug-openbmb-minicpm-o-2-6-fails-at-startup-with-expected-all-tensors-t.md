# vllm-project/vllm#42322: [Bug]: openbmb/MiniCPM-o-2_6 fails at startup with `Expected all tensors to be on the same device, but found at least two devices`

| 字段 | 值 |
| --- | --- |
| Issue | [#42322](https://github.com/vllm-project/vllm/issues/42322) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: openbmb/MiniCPM-o-2_6 fails at startup with `Expected all tensors to be on the same device, but found at least two devices`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm` installed with `uv pip install https://github.com/vllm-project/vllm/releases/download/v0.20.1/vllm-0.20.1+cu129-cp38-abi3-manylinux_2_31_x86_64.whl --torch-backend=cu129` because I'm on Almalinux 9 so there is no way to get CUDA 13 wheels on this OS. Running `vllm serve openbmb/MiniCPM-o-2_6 --trust-remote-code --max-model-len=16000` fails with ``` RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! ``` Full log ``` (APIServer pid=63409) INFO 05-11 12:56:04 [utils.py:299] (APIServer pid=63409) INFO 05-11 12:56:04 [utils.py:299] █ █ █▄ ▄█ (APIServer pid=63409) INFO 05-11 12:56:04 [utils.py:299] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.20.1 (APIServer pid=63409) INFO 05-11 12:56:04 [utils.py:299] █▄█▀ █ █ █ █ model openbmb/MiniCPM-o-2_6 (APIServer pid=63409) INFO 05-11 12:56:04 [utils.py:299] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=63409) INFO 05-11 12:56:04 [utils.py:299] (APIServer pid=63409) INFO 05-11 12:56:04 [utils.py:233] non-default args: {'model_tag': 'openbmb/MiniCPM-o-2_6', 'model': 'openbmb/MiniCPM-o-2_6', 'trust_remote_code': True, 'max_model_len': 16000} (APIServer pid=6340...

## 现有链接修复摘要

#42332 [Bugfix] Fixes MiniCPM-O resampler device placement to avoid tensor device mismatch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ces` bug ### Your current environment ### 🐛 Describe the bug `vllm` installed with `uv pip install https://github.com/vllm-project/vllm/releases/download/v0.20.1/vllm-0.20.1+cu129-cp38-abi3-manylinux_2_31_x86_64.whl --t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: ad/v0.20.1/vllm-0.20.1+cu129-cp38-abi3-manylinux_2_31_x86_64.whl --torch-backend=cu129` because I'm on Almalinux 9 so there is no way to get CUDA 13 wheels on this OS. Running `vllm serve openbmb/MiniCPM-o-2_6 --trust-r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: OS. Running `vllm serve openbmb/MiniCPM-o-2_6 --trust-remote-code --max-model-len=16000` fails with ``` RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! ``` Fu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ng in `AutoImageProcessor` instead. (APIServer pid=63409) [transformers] Requested torchvision backend is not available. Falling back to pil backend. (APIServer pid=63409) [transformers] `MiniCPMOProcessor` defines `fea...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=16000, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42332](https://github.com/vllm-project/vllm/pull/42332) | closes_keyword | 0.95 | [Bugfix] Fixes MiniCPM-O resampler device placement to avoid tensor device mismatch | fix, engine core fails to start during the profile run with the same trace as in #42322. After applying the fix, the engine core initialises successfully, weights load, and the |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
