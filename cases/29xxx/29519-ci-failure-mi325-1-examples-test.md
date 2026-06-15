# vllm-project/vllm#29519: [CI Failure]: mi325_1: Examples Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29519](https://github.com/vllm-project/vllm/issues/29519) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;sampling |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Examples Test

### Issue 正文摘录

### Name of failing test `pip install tensorizer && python3 offline_inference/basic/generate.py --model facebook/opt-125m && python3 offline_inference/basic/generate.py --model meta-llama/Llama-2-13b-chat-hf --cpu-offload-gb 10 && python3 offline_inference/basic/chat.py && python3 offline_inference/prefix_caching.py && python3 offline_inference/llm_engine_example.py && python3 offline_inference/audio_language.py --seed 0 && python3 offline_inference/vision_language.py --seed 0 && python3 offline_inference/vision_language_pooling.py --seed 0 && python3 offline_inference/vision_language_multi_image.py --seed 0 && python3 others/tensorize_vllm_model.py --model facebook/opt-125m serialize --serialized-directory /tmp/ --suffix v1 && python3 others/tensorize_vllm_model.py --model facebook/opt-125m deserialize --path-to-tensors /tmp/vllm/facebook/opt-125m/v1/model.tensors && python3 offline_inference/encoder_decoder_multimodal.py --model-type whisper --seed 0 && python3 offline_inference/basic/classify.py && python3 offline_inference/basic/embed.py && python3 offline_inference/basic/score.py && python3 offline_inference/spec_decode.py --test --method eagle --num_spec_tokens 3 --dataset-n...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: `pip install tensorizer && python3 offline_inference/basic/generate.py --model facebook/opt-125m && python3 offline_inference/basic/generate.py --model meta-llama/Llama-2-13b-chat-hf --cpu-offload-gb 10 && python3 offli...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: Examples Test ci-failure ### Name of failing test `pip install tensorizer && python3 offline_inference/basic/generate.py --model facebook/opt-125m && python3 offline_inference/basic/generate.py --m
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: lyAttention layer in BERT model **Configuration:** - Model: intfloat/e5-small (BERT-based embedding model) - Runner: pooling - enforce_eager: True **Stack trace:** 1. LLM initialization → LLMEngine.from_engine_args 2. E...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: /facebook/opt-125m/v1/model.tensors && python3 offline_inference/encoder_decoder_multimodal.py --model-type whisper --seed 0 && python3 offline_inference/basic/classify.py && python3 offline_inference/basic/embed.py &&...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: r:** `NotImplementedError: Encoder self-attention is not implemented for TritonAttentionImpl` - Location: vllm/v1/attention/backends/triton_attn.py line 251 - During initialization of EncoderOnlyAttention layer in BERT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
