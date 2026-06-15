# vllm-project/vllm#18757: [Bug]: model_executor/test_model_load_with_params.py  fails with AttributeError

| 字段 | 值 |
| --- | --- |
| Issue | [#18757](https://github.com/vllm-project/vllm/issues/18757) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: model_executor/test_model_load_with_params.py  fails with AttributeError

### Issue 正文摘录

### Your current environment Issue encountered on main branch tests. ### 🐛 Describe the bug Test failing with below traceback: ``` vllm_runner = @pytest.mark.skipif(current_platform.is_rocm(), reason="Xformers backend is not supported on ROCm.") def test_model_loading_with_params(vllm_runner): """ Test parameter weight loading with tp>1. """ with vllm_runner(model_name=MODEL_NAME, revision=REVISION, dtype="float16", max_model_len=MAX_MODEL_LEN) as vllm_model: output = vllm_model.encode("Write a short story about a robot that" " dreams for the first time.\n") model_config = vllm_model.model.llm_engine.model_config model_tokenizer = vllm_model.model.llm_engine.tokenizer # asserts on the bert model config file assert model_config.encoder_config["max_seq_length"] == 512 assert model_config.encoder_config["do_lower_case"] # asserts on the pooling config files assert model_config.pooler_config.pooling_type == PoolingType.CLS.name > assert model_config.pooler_config.pooling_norm E AttributeError: 'PoolerConfig' object has no attribute 'pooling_norm'. Did you mean: 'pooling_type'? tests/model_executor/test_model_load_with_params.py:43: AttributeError --------------------------------------...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ME, revision=REVISION, dtype="float16", max_model_len=MAX_MODEL_LEN) as vllm_model: output = vllm_model.encode("Write a short story about a robot that" " dreams for th
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: eback: ``` vllm_runner = @pytest.mark.skipif(current_platform.is_rocm(), reason="Xformers backend is not supported on ROCm.") def test_model_loading_with_params(vllm_runner): """ Test parameter weight loading with tp>1....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: dev148+gfba064270.d20250526) with config: model='BAAI/bge-base-en-v1.5', speculative_config=None, tokenizer='BAAI/bge-base-en-v1.5', skip_tokenizer_init=False, tokenizer_mode=auto, revision=main, override_neuron_config=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: pif(current_platform.is_rocm(), reason="Xformers backend is not supported on ROCm.") def test_model_loading_with_params(vllm_runner): """ Test parameter weight loading with tp>1. """ with vllm_runner(model_name=MODEL_NA...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nd=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=BAAI/bge-base-en-v1.5, num_scheduler_steps=1, mu...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
