# vllm-project/vllm#22344: [Bug]: RuntimeError: _vllm_fa2_C::varlen_fwd() expected at most 21 argument(s) but received 22 argument(s).

| 字段 | 值 |
| --- | --- |
| Issue | [#22344](https://github.com/vllm-project/vllm/issues/22344) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: _vllm_fa2_C::varlen_fwd() expected at most 21 argument(s) but received 22 argument(s).

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CMD : ```vllm serve "/root/llm/models/qwen3/awq/32B" --served-model-name "qwen3-32b" --api-key "xxxxx" --load-format "safetensors" --port 8000 --host 0.0.0.0 --gpu_memory_utilization 0.95 --tensor-parallel-size 1 --block-size 16 --enforce-eager --max-model-len 16384 --max-num-batched-tokens 32768 --max-num-seqs 100 --tool-call-parser hermes --enable-auto-tool-choice``` + **version** : 0.9.1.dev186+gda4038021.d20250606 **OK**. + **version** : 0.10.1.dev388+g796bae07c.d20250806 **ERROR**. **ERROR**: ``` (EngineCore_0 pid=23119) RuntimeError: _vllm_fa2_C::varlen_fwd() expected at most 21 argument(s) but received 22 argument(s). Declaration: _vllm_fa2_C::varlen_fwd(Tensor($0! -> ) q, Tensor k, Tensor v, Tensor($1! -> )? out, Tensor cu_seqlens_q, Tensor cu_seqlens_k, Tensor? seqused_k, Tensor? leftpad_k, Tensor? block_table, Tensor? alibi_slopes, int max_seqlen_q, int max_seqlen_k, float p_dropout, float softmax_scale, bool zero_tensors, bool is_causal, int window_size_left, int window_size_right, float softcap, bool return_softmax, Generator? gen) -> Tensor[] [rank0]:[W806 16:39:40.789551293 ProcessGroupNCCL.cpp:1522] Warning: WARNIN...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: num-seqs 100 --tool-call-parser hermes --enable-auto-tool-choice``` + **version** : 0.9.1.dev186+gda4038021.d20250606 **OK**. + **version** : 0.10.1.dev388+g796bae07c.d20250806 **ERROR**. **ERROR**: ``` (EngineCore_0 pi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: opes, int max_seqlen_q, int max_seqlen_k, float p_dropout, float softmax_scale, bool zero_tensors, bool is_causal, int window_size_left, int window_size_right, float softcap, bool return_softmax, Generator? gen) -> Tens...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nvironment ### 🐛 Describe the bug CMD : ```vllm serve "/root/llm/models/qwen3/awq/32B" --served-model-name "qwen3-32b" --api-key "xxxxx" --load-format "safetensors" --port 8000 --host 0.0.0.0 --gpu_memory_utilization 0....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: --host 0.0.0.0 --gpu_memory_utilization 0.95 --tensor-parallel-size 1 --block-size 16 --enforce-eager --max-model-len 16384 --max-num-batched-tokens 32768 --max-num-seqs 100 --tool-call-parser hermes --enable-auto-tool-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
