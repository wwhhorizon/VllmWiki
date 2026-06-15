# vllm-project/vllm#12855: [Bug]: BNB models not working in 0.7.1 version - `got an unexpected keyword argument 'kv_data_type'`

| 字段 | 值 |
| --- | --- |
| Issue | [#12855](https://github.com/vllm-project/vllm/issues/12855) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: BNB models not working in 0.7.1 version - `got an unexpected keyword argument 'kv_data_type'`

### Issue 正文摘录

### Discussed in https://github.com/vllm-project/vllm/discussions/12849 Originally posted by **davefojtik** February 6, 2025 In **0.7.0** everything works fine. But when I update to **0.7.1** with the same models, code etc. it's broken. The logs spam a lot of `MLA is not supported with bitsandbytes quantization. Disabling MLA.`, even though the `VLLM_MLA_DISABLE` env variable is set to true. Then after the `Capturing cudagraphs` part, the vllm returns the following error: ``` "Uncaught exception | ; BatchDecodeWithPagedKVCacheWrapper.plan() got an unexpected keyword argument 'kv_data_type'; ; ``` Every update I go through the engine arguments and enviroment variables in the documentation to see if there's something new or changed, but this time I didn't see anything that could cause this. Did I miss some major change? Here's the full log (we're using custom VLLM on RunPod serverless): ```text INFO 02-06 04:28:25 __init__.py:183] Automatically detected platform cuda. Starting Job... VLLM Engine not initialized, starting... WARNING 02-06 04:28:31 config.py:605] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. WARNING 02-06 04:2...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: broken. The logs spam a lot of `MLA is not supported with bitsandbytes quantization. Disabling MLA.`, even though the `VLLM_MLA_DISABLE` env variable is set to true. Then after the `Capturing cudagraphs` part, the vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: the vllm returns the following error: ``` "Uncaught exception | ; BatchDecodeWithPagedKVCacheWrapper.plan() got an unexpected keyword argument 'kv_data_type'; ; ``` Every update I go through the engine arguments and env...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: BNB models not working in 0.7.1 version - `got an unexpected keyword argument 'kv_data_type'` ### Discussed in https://github.com/vllm-project/vllm/discussions/12849 Originally posted by **davefojtik** February 6...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: er='/workspace/models/Lamarck-14B-v0.7-bnb-4bit/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=main, override_neuron_config=None, tokenizer_revision=main, trust_remote_code=True, dtype=torch.bfloat16, max_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: BNB models not working in 0.7.1 version - `got an unexpected keyword argument 'kv_data_type'` ### Discussed in https://github.com/vllm-project/vllm/discussions/12849 Originally posted by **davefojtik** February 6...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
