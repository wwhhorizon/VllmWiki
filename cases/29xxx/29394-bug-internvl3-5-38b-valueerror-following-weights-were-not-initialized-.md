# vllm-project/vllm#29394: [Bug]: InternVL3_5-38B: ValueError: Following weights were not initialized from checkpoint:

| 字段 | 值 |
| --- | --- |
| Issue | [#29394](https://github.com/vllm-project/vllm/issues/29394) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL3_5-38B: ValueError: Following weights were not initialized from checkpoint:

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```shell vllm serve ${model_path} --served-model-name InternVL3_5-38B --port 40001 --host 127.0.0.1 --dtype bfloat16 --trust-remote-code --tensor-parallel-size 2 ``` Error: ``` raise ValueError( (Worker_TP0 pid=85304) ERROR 11-25 17:57:23 [multiproc_executor.py:743] ValueError: Following weights were not initialized from checkpoint: {'language_model.model.layers.2.mlp.down_proj.weight', 'language_model.model.layers.17.post_attention_layernorm.weight', 'language_model.model.layers.5.self_attn.o_proj.weight', 'language_model.model.layers.22.self_attn.k_norm.weight', 'language_model.model.layers.22.self_attn.qkv_proj.weight', 'language_model.model.layers.20.mlp.gate_up_proj.weight', 'language_model.model.layers.18.mlp.down_proj.weight', 'language_model.model.layers.3.input_layernorm.weight', 'language_model.model.layers.3.mlp.down_proj.weight', 'language_model.model.layers.21.self_attn.qkv_proj.weight', 'language_model.model.layers.21.self_attn.o_proj.weight', 'language_model.model.layers.6.input_layernorm.weight', 'language_model.model.layers.5.mlp.down_proj.weight', 'language_model.model.layers.18.input_layernorm.weight', 'languag...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support cuda;operator;triton build_error dtype;env_dependency Your c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ath} --served-model-name InternVL3_5-38B --port 40001 --host 127.0.0.1 --dtype bfloat16 --trust-remote-code --tensor-parallel-size 2 ``` Error: ``` raise ValueError( (Worker_TP0 pid=85304) ERROR 11-25 17:57:23 [multipro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: InternVL3_5-38B: ValueError: Following weights were not initialized from checkpoint: bug ### Your current environment ### 🐛 Describe the bug ```shell vllm serve ${model_path} --served-model-name InternVL3_5-38B -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el;frontend_api;gemm_linear;hardware_porting;model_support cuda;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
