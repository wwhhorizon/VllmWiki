# vllm-project/vllm#39314: [Bug]: MiniMax-M2.5-NVFP4: KeyError 'layers.0.self_attn.qkv_proj.k_scale' during load_weights — checkpoint uses split q/k/v, loader expects fused qkv_proj

| 字段 | 值 |
| --- | --- |
| Issue | [#39314](https://github.com/vllm-project/vllm/issues/39314) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | wrong_output |
| Operator 关键词 | attention;fp8;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniMax-M2.5-NVFP4: KeyError 'layers.0.self_attn.qkv_proj.k_scale' during load_weights — checkpoint uses split q/k/v, loader expects fused qkv_proj

### Issue 正文摘录

### Your current environment vLLM: 0.18.0 (image: vllm/vllm-audio:v0.18.0 or equivalent) Model: (full main snapshot) GPU: NVIDIA H200 NVL, tensor_parallel_size=4 Quantization: ModelOpt NVFP4 (as detected by vLLM: Detected ModelOpt NVFP4 checkpoint) ### 🐛 Describe the bug Summary Loading nvidia/MiniMax-M2.5-NVFP4 from a full Hugging Face–style directory (29 safetensors shards + model.safetensors.index.json) fails during load_weights with: KeyError: 'layers.0.self_attn.qkv_proj.k_scale' The index file does not contain any qkv_proj tensors; attention weights use separate q_proj, k_proj, and v_proj (e.g. model.layers.0.self_attn.k_proj.k_scale). So this looks like a loader / checkpoint layout mismatch, not a missing or corrupted file. python3 -m vllm.entrypoints.openai.api_server \ --model /path/to/MiniMax-M2.5-NVFP4 \ --trust-remote-code \ --tensor-parallel-size 4 \ --kv-cache-dtype fp8 \ --tool-call-parser minimax_m2 \ --enable-auto-tool-choice Actual behavior Engine startup fails while workers load weights. Stack trace includes: ``` File ".../vllm/model_executor/models/minimax_m2.py", line 442, in load_weights param = params_dict[name] KeyError: 'layers.0.self_attn.qkv_proj.k_scale...

## 现有链接修复摘要

#39430 fix(minimax_m2): avoid KeyError on split q/k/v NVFP4 weight scales

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: MiniMax-M2.5-NVFP4: KeyError 'layers.0.self_attn.qkv_proj.k_scale' during load_weights — checkpoint uses split q/k/v, loader expects fused qkv_proj bug ### Your current environment vLLM: 0.18.0 (image: vllm/vllm-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: _attn.k_proj.k_scale). So this looks like a loader / checkpoint layout mismatch, not a missing or corrupted file. python3 -m vllm.entrypoints.openai.api_server \ --model /path/to/MiniMax-M2.5-NVFP4 \ --trust-remote-code...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: environment vLLM: 0.18.0 (image: vllm/vllm-audio:v0.18.0 or equivalent) Model: (full main snapshot) GPU: NVIDIA H200 NVL, tensor_parallel_size=4 Quantization: ModelOpt NVFP4 (as detected by vLLM: Detected ModelOpt NVFP4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: oj.k_scale' ``` Expected behavior Weights load successfully for the official nvidia/MiniMax-M2.5-NVFP4 checkpoint, or documentation clearly states a minimum vLLM commit / image and any required conversion if the public...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rs.0.self_attn.k_proj.k_scale). So this looks like a loader / checkpoint layout mismatch, not a missing or corrupted file. python3 -m vllm.entrypoints.openai.api_server \ --model /path/to/MiniMax-M2.5-NVFP4 \ --trust-re...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39430](https://github.com/vllm-project/vllm/pull/39430) | closes_keyword | 0.95 | fix(minimax_m2): avoid KeyError on split q/k/v NVFP4 weight scales | Fixes #39314 When loading the checkpoint (or any checkpoint that stores attention weights as separate `q_proj`, `k_proj`, `v_proj` rather than fused `qkv_proj`), `MiniMaxM2Model. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
