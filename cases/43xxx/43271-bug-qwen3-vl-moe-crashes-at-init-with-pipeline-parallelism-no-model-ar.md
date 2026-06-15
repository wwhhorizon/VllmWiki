# vllm-project/vllm#43271: [Bug]: Qwen3-VL-MoE crashes at init with pipeline parallelism ("No model architectures are specified")

| 字段 | 值 |
| --- | --- |
| Issue | [#43271](https://github.com/vllm-project/vllm/issues/43271) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | moe;quantization |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-MoE crashes at init with pipeline parallelism ("No model architectures are specified")

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Serving a Qwen3-VL-MoE model with `--pipeline-parallel-size 2` fails during engine initialization with a pydantic `ValidationError`: ``` File ".../vllm/model_executor/models/qwen3_vl_moe.py", line 450, in __init__ vllm_config=vllm_config.with_hf_config(config.text_config), File ".../vllm/config/vllm.py", line 593, in with_hf_config return replace(self, model_config=model_config) File ".../vllm/config/utils.py", line 127, in replace return cls(**dataclass_dict) pydantic_core._pydantic_core.ValidationError: 1 validation error for VllmConfig Value error, No model architectures are specified ``` Reproduces with `pipeline_parallel_size > 1`; does **not** occur with `--tensor-parallel-size 2 --pipeline-parallel-size 1`. ### Root cause `Qwen3VLMoeForConditionalGeneration.__init__` builds the inner language model from the text sub-config: ```python self.language_model = Qwen3MoeLLMForCausalLM( vllm_config=vllm_config.with_hf_config(config.text_config), prefix=maybe_prefix(prefix, "language_model"), ) ``` For these checkpoints `config.text_config.architectures is None` (architectures only exist on the top-level config). `with_hf_config()`...

## 现有链接修复摘要

#43272 [Bugfix] Qwen3-VL(-MoE): pass architectures to with_hf_config for pipeline parallelism

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-VL-MoE crashes at init with pipeline parallelism ("No model architectures are specified") ### Your current environment ### 🐛 Describe the bug Serving a Qwen3-VL-MoE model with `--pipeline-parallel-size 2` f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rashes at init with pipeline parallelism ("No model architectures are specified") ### Your current environment ### 🐛 Describe the bug Serving a Qwen3-VL-MoE model with `--pipeline-parallel-size 2` fails during engine in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Qwen3-VL-MoE crashes at init with pipeline parallelism ("No model architectures are specified") ### Your current environment ### 🐛 Describe the bug Serving a Qwen3-VL-MoE model with `--pipeline-parallel-size 2` f...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: for VllmConfig Value error, No model architectures are specified ``` Reproduces with `pipeline_parallel_size > 1`; does **not** occur with `--tensor-parallel-size 2 --pipeline-parallel-size 1`. ### Root cause `Qwen3VLMo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: and existing issues. development distributed_parallel;model_support;moe;quantization moe;quantization crash env_dependency #43272 [Bugfix] Qwen3-VL(-MoE): pass architectures to with_hf_config for pipeline parallelism Yo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43272](https://github.com/vllm-project/vllm/pull/43272) | closes_keyword | 0.95 | [Bugfix] Qwen3-VL(-MoE): pass architectures to with_hf_config for pipeline parallelism | Fixes #43271. Qwen3-VL-MoE (and dense Qwen3-VL) crash at engine init with `--pipeline-parallel-size > 1`: ``` pydantic_core._pydantic_core.ValidationError: 1 validation error for |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
