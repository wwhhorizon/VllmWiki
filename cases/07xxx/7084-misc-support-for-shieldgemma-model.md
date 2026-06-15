# vllm-project/vllm#7084: [Misc]: Support for Shieldgemma model

| 字段 | 值 |
| --- | --- |
| Issue | [#7084](https://github.com/vllm-project/vllm/issues/7084) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Support for Shieldgemma model

### Issue 正文摘录

### Trying to run the Shieldgemma model. The architecture is Gemma2ForCausalLM which should be already supported. The config file specifies the transformers version to be 4.42.4. I have the following installed: ``` pip list | grep "vllm\|flash" flash-attn 2.0.4 flashinfer 0.1.3+cu124torch2.4 vllm 0.5.3.post1 vllm-flash-attn 2.5.9.post1 ``` I have also the Transformers 4.43.3. After checking the config file, it appears that the config specifies `hidden_activation` instead of `hidden_act`. After changing it manually in the config.json file, I get an error which specifies that I should use flashinfer backend. `VLLM_ATTENTION_BACKEND=FLASHINFER ` After which, the following error is occurring: ``` INFO 08-02 17:46:35 llm_engine.py:176] Initializing an LLM engine (v0.5.3.post1) with config: model='/modelcache/models--google--shieldgemma-2b/snapshots/091a5128690e57ca6a30f6fbec4a766d8b77e48d', speculative_config=None, tokenizer='/modelcache/models--google--shieldgemma-2b/snapshots/091a5128690e57ca6a30f6fbec4a766d8b77e48d', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Gemma2ForCausalLM which should be already supported. The config file specifies the transformers version to be 4.42.4. I have the following installed: ``` pip list | grep "vllm\|flash" flash-attn 2.0.4 flashinfer 0.1.3+c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Misc]: Support for Shieldgemma model ### Trying to run the Shieldgemma model. The architecture is Gemma2ForCausalLM which should be already supported. The config file specifies the transformers version to be 4.42.4. I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: `` pip list | grep "vllm\|flash" flash-attn 2.0.4 flashinfer 0.1.3+cu124torch2.4 vllm 0.5.3.post1 vllm-flash-attn 2.5.9.post1 ``` I have also the Transformers 4.43.3. After checking the config file
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: port for Shieldgemma model ### Trying to run the Shieldgemma model. The architecture is Gemma2ForCausalLM which should be already supported. The config file specifies the transformers version to be 4.42.4. I have the fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
