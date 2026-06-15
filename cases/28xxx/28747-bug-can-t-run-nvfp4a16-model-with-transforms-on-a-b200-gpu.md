# vllm-project/vllm#28747: [Bug]: Can't run NVFP4A16 model with transforms on a B200 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#28747](https://github.com/vllm-project/vllm/issues/28747) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't run NVFP4A16 model with transforms on a B200 GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Recipe to create the model: ```python from transformers import AutoModelForCausalLM, AutoTokenizer from llmcompressor import oneshot from llmcompressor.modifiers.quantization import QuantizationModifier from llmcompressor.modifiers.transform import SpinQuantModifier from llmcompressor.utils import dispatch_for_generation # Select model and load it. MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct" model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype="auto") tokenizer = AutoTokenizer.from_pretrained(MODEL_ID) recipe = [ SpinQuantModifier( rotations=["R1", "R2", "R4"], transform_block_size=16, transform_type="hadamard", ), QuantizationModifier(targets="Linear", scheme="NVFP4A16", ignore=["lm_head"]), ] # Apply algorithms. oneshot(model=model, recipe=recipe, pipeline="datafree") # Save to disk compressed. SAVE_DIR = MODEL_ID.split("/")[1] + "-spinquantR1R2R4-nvfp4a16" model.save_pretrained(SAVE_DIR, save_compressed=True) tokenizer.save_pretrained(SAVE_DIR) ``` `llmcompressor` (0.8.1) installed from pypi with: `uv pip install llmcompressor` Command to reproduce the issue on a B200 node (on H100 everything looks fine): ```ba...

## 现有链接修复摘要

#43462 [Bugfix] hadacore_transform: respect inplace parameter to fix garbage outputs with QuIP transforms

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: Can't run NVFP4A16 model with transforms on a B200 GPU bug ### Your current environment ### 🐛 Describe the bug Recipe to create the model: ```python from transformers import AutoModelForCausalLM, AutoTokenizer fr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: B200 GPU bug ### Your current environment ### 🐛 Describe the bug Recipe to create the model: ```python from transformers import AutoModelForCausalLM, AutoTokenizer from llmcompressor import oneshot from llmcompressor.mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: fiers.transform import SpinQuantModifier from llmcompressor.utils import dispatch_for_generation # Select model and load it. MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct" model = AutoModelForCausalLM.from_pretrained(MOD...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Can't run NVFP4A16 model with transforms on a B200 GPU bug ### Your current environment ### 🐛 Describe the bug Recipe to create the model: ```python from transformers import AutoModelForCausalLM, AutoTokenizer fr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Can't run NVFP4A16 model with transforms on a B200 GPU bug ### Your current environment ### 🐛 Describe the bug Recipe to create the model: ```python from transformers import AutoModelForCausalLM, AutoTokenizer fr...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43462](https://github.com/vllm-project/vllm/pull/43462) | closes_keyword | 0.95 | [Bugfix] hadacore_transform: respect inplace parameter to fix garbage outputs with QuIP transforms | fix (@kylesayrs); this PR addresses the remaining SM120 case at kernel level - #28748: build coverage for Blackwell (@mgoin) - #28747: B200 build issue (@eldarkurtic) - #22486: |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
