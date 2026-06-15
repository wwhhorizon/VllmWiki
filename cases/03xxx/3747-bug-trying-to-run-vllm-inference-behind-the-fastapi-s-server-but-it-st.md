# vllm-project/vllm#3747: [Bug]: trying to run vllm inference behind the fastapi's server, but it stucks

| 字段 | 值 |
| --- | --- |
| Issue | [#3747](https://github.com/vllm-project/vllm/issues/3747) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: trying to run vllm inference behind the fastapi's server, but it stucks

### Issue 正文摘录

### Your current environment A100 x 8, ubuntu ### 🐛 Describe the bug hello, I am trying to run `vllm` inference behind the fastapi's server, but it stucks at `Using model weights format ['*.safetensors']`. Are there anyone experiencing such a case? ``` 2024-03-31 02:05:20,110 INFO sqlalchemy.engine.Engine COMMIT INFO: Application startup complete. INFO: Uvicorn running on http://0.0.0.0:8009 (Press CTRL+C to quit) 2024-03-31 02:05:21,902 INFO worker.py:1752 -- Started a local Ray instance. /home/sionic/sigrid/logickor-pipeline/logickor_uv_pipeline/services/generator.py:21: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]` SINGLE_TURN_TEMPLATE, DOUBLE_TURN_TEMPLATE = df_config[0], df_config[1] INFO 03-31 02:05:23 config.py:433] Custom all-reduce kernels are temporarily disabled due to stability issues. We will re-enable them once the issues are resolved. 2024-03-31 02:05:23,253 INFO worker.py:1585 -- Calling ray.init() again after it has already been called. INFO 03-31 02:05:23 llm_engine.py:87] Initial...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: `Using model weights format ['*.safetensors']`. Are there anyone experiencing such a case? ``` 2024-03-31 02:05:20,110 INFO sqlalchemy.engine.Engine COMMIT INFO: Application startup complete. INFO: Uvicorn running on ht...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=4, disable_custom_all_reduce=True, quantization=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nd the fastapi's server, but it stucks bug ### Your current environment A100 x 8, ubuntu ### 🐛 Describe the bug hello, I am trying to run `vllm` inference behind the fastapi's server, but it stucks at `Using model weigh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: un `vllm` inference behind the fastapi's server, but it stucks at `Using model weights format ['*.safetensors']`. Are there anyone experiencing such a case? ``` 2024-03-31 02:05:20,110 INFO sqlalchemy.engine.Engine COMM...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=4, disable_custom_all_reduce=True, quantiza...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
