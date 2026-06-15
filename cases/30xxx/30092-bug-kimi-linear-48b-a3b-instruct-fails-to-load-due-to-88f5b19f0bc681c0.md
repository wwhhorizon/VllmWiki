# vllm-project/vllm#30092: [Bug]: Kimi-Linear-48B-A3B-Instruct fails to load due to 88f5b19f0bc681c016eaaa17502d3bb4e2b59b51

| 字段 | 值 |
| --- | --- |
| Issue | [#30092](https://github.com/vllm-project/vllm/issues/30092) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi-Linear-48B-A3B-Instruct fails to load due to 88f5b19f0bc681c016eaaa17502d3bb4e2b59b51

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve fails for moonshotai/Kimi-Linear-48B-A3B-Instruct due to 88f5b19f0bc681c016eaaa17502d3bb4e2b59b51 ``` vllm serve ./huggingface/moonshotai/Kimi-Linear-48B-A3B-Instruct \ --port 8000 \ --tensor-parallel-size 1 \ --max-model-len 1048576 \ --trust-remote-code (APIServer pid=13676) INFO 12-04 22:39:35 [api_server.py:1338] vLLM API server version 0.11.2.dev520+g1109f9828.d20251204 (APIServer pid=13676) INFO 12-04 22:39:35 [utils.py:253] non-default args: {'model_tag': './huggingface/moonshotai/Kimi-Linear-48B-A3B-Instruct', 'model': './huggingface/moonshotai/Kimi-Linear-48B-A3B-Instruct', 'trust_remote_code': True, 'max_model_len': 1048576} (APIServer pid=13676) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=13676) INFO 12-04 22:39:35 [model.py:636] Resolved architecture: KimiLinearForCausalLM (APIServer pid=13676) INFO 12-04 22:39:35 [model.py:1749] Using max model len 1048576 (APIServer pid=13676) INFO 12-04 22:39:35 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=13676) INFO 12-04 22:39:35 [config.py:315]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rver pid=13676) INFO 12-04 22:39:35 [api_server.py:1338] vLLM API server version 0.11.2.dev520+g1109f9828.d20251204 (APIServer pid=13676) INFO 12-04 22:39:35 [utils.py:253] non-default args: {'model_tag': './huggingface...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=1048576, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_si...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: IServer pid=13676) INFO 12-04 22:39:35 [config.py:439] Setting attention block size to 1920 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=13676) INFO 12-04 22:39:35 [config.py:463] Padd...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nstruct due to 88f5b19f0bc681c016eaaa17502d3bb4e2b59b51 ``` vllm serve ./huggingface/moonshotai/Kimi-Linear-48B-A3B-Instruct \ --port 8000 \ --tensor-parallel-size 1 \ --max-model-len 1048576 \ --trust-remote-code (APIS...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
