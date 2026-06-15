# vllm-project/vllm#19076: [Bug]: Maybe vllm using float16 inference is less precise than transformer using float16 inference????

| 字段 | 值 |
| --- | --- |
| Issue | [#19076](https://github.com/vllm-project/vllm/issues/19076) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;model_support |
| 子分类 | debug |
| Operator 关键词 | activation;attention;cuda;moe |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Maybe vllm using float16 inference is less precise than transformer using float16 inference????

### Issue 正文摘录

PTAL #18940 sentence_transformer and vllm's float16 models are exactly the same, but the results are different. vllm's float32 models results are the same as sentence_transformer ### 🐛 Describe the bug ```python import torch from tests.conftest import HfRunner from tests.models.language.pooling.mteb_utils import run_mteb_embed_task, MTEB_EMBED_TASKS, VllmMtebEncoder model = "thenlper/gte-large" hf_model = HfRunner( model, dtype="float16", is_sentence_transformer=True, ) st_main_score = run_mteb_embed_task(hf_model, MTEB_EMBED_TASKS) # 0.7680302125398653 print(hf_model.model[0].auto_model.encoder.layer[0].intermediate.dense.weight) """ hf_model.model[0].auto_model.encoder.layer[0].intermediate.dense.weight Parameter containing: tensor([[ 0.0728, -0.0249, 0.0490, ..., 0.0595, 0.0363, 0.0181], [ 0.0327, 0.0181, 0.0223, ..., 0.0534, -0.0257, 0.0275], [-0.0246, 0.0504, 0.0197, ..., 0.0159, -0.0805, 0.0060], ..., [ 0.0048, 0.0043, -0.0147, ..., 0.0363, -0.0344, 0.0045], [ 0.0347, 0.0642, -0.0393, ..., 0.0238, 0.0541, 0.0966], [-0.0337, 0.0023, 0.0086, ..., -0.0003, -0.0105, -0.0164]], device='cuda:0', dtype=torch.float16, requires_grad=True) """ from tests.conftest import VllmRunner vll...

## 现有链接修复摘要

#18940 [Core] hybrid dtype for Pooling Models: float32 for weights and activation, float16 or bfloat16 for attention.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Maybe vllm using float16 inference is less precise than transformer using float16 inference???? bug PTAL #18940 sentence_transformer and vllm's float16 models are exactly the same, but the results are different....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Maybe vllm using float16 inference is less precise than transformer using float16 inference???? bug PTAL #18940 sentence_transformer and vllm's float16 models are exactly the same, but the results are different....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: inference???? bug PTAL #18940 sentence_transformer and vllm's float16 models are exactly the same, but the results are different. vllm's float32 models results are the same as sentence_transformer ### 🐛 Describe the bug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 337, 0.0023, 0.0086, ..., -0.0003, -0.0105, -0.0164]], device='cuda:0', dtype=torch.float16, requires_grad=True) """ from tests.conftest import VllmRunner vllm_model = VllmRunner(model, task="embed", max_model_len=None,...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: e to the mlp layer. I can't find out why the precise has decreased, ask experts for help. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at th...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18940](https://github.com/vllm-project/vllm/pull/18940) | mentioned | 0.45 | [Core] hybrid dtype for Pooling Models: float32 for weights and activation, float16 or bfloat16 for attention.  | ce is less precise than transformer using float16 inference???? ptal #18940 sentence_transformer and vllm's float16 models are exactly the same, but the results are different. vll… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
