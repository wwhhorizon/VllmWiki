# vllm-project/vllm#39532: [Bug]: `_CONFIG_REGISTRY` types get wrong config class since v0.19

| 字段 | 值 |
| --- | --- |
| Issue | [#39532](https://github.com/vllm-project/vllm/issues/39532) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cuda;moe;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `_CONFIG_REGISTRY` types get wrong config class since v0.19

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When a vLLM plugin registers a custom config class via `AutoConfig.register()` and the user passes `hf_overrides={"model_type": " "}`, the resulting config object is the **wrong class**. The `model_type` from `hf_overrides` is used for vLLM's internal `_CONFIG_REGISTRY` lookup, but `AutoConfig.from_pretrained()` independently reads `model_type` from the checkpoint's `config.json` file on disk and uses *that* to determine the Python class. This means: - If the checkpoint says `model_type: "mixtral"` but the plugin registers `model_type: "mymodel"` → `AutoConfig.from_pretrained()` returns `MixtralConfig`, not `MyModelConfig` - `hf_overrides` are applied *after* config creation (`config.update(hf_overrides_kw)`), so `config.model_type` gets updated to `"mymodel"` but the **Python class remains `MixtralConfig`** - All custom attributes defined in `MyModelConfig.__init__` are missing from the config object ### Root cause **Note:** This is not a transformers/`AutoConfig` bug. `AutoConfig.from_pretrained()` resolving the class from the on-disk `model_type` is working as designed. The bug is in vLLM's `HFConfigParser.parse()`, which swit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: through vLLM's `get_config()` — the actual broken code path: ```python import json, os, tempfile from transformers import PretrainedConfig from vllm.transformers_utils.config import _CONFIG_REGISTRY, get_config class My...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Impact This affects any vLLM plugin that: 1. Defines a custom model architecture with its own config class 2. Has checkpoints that use a different `model_type` on disk (e.g., derived from an existing architecture li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: `_CONFIG_REGISTRY` types get wrong config class since v0.19 bug ### Your current environment ### 🐛 Describe the bug When a vLLM plugin registers a custom config class via `AutoConfig.register()` and the user pass...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: num_key_value_heads": 4, "intermediate_size": 256, "num_local_experts": 4, "num_experts_per_tok": 2} with open(os.path.join(tmpdir, "config.json"), "w") as f: json.dump(cfg, f) config = get_config(tmpdir, trust_remote_c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: NFIG_REGISTRY`. The `AutoConfig.register()` call achieves that goal, but routing the primary config loading through `AutoConfig.from_pretrained()` instead of `config_class.from_pretrained()` broke the case where the che...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
