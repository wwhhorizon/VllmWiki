# vllm-project/vllm#14677: [Bug]: Unit test `tests/models/embedding/vision_language/test_phi3v.py` failing

| 字段 | 值 |
| --- | --- |
| Issue | [#14677](https://github.com/vllm-project/vllm/issues/14677) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unit test `tests/models/embedding/vision_language/test_phi3v.py` failing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug BUG: unittest `tests/models/embedding/vision_language/test_phi3v.py` is failiing After installing vllm, run `pytest -sv tests/models/embedding/vision_language/test_phi3v.py::test_models_image[half-TIGER-Lab/VLM2Vec-Full]` A snippet of unittest failure log ``` tests/models/embedding/vision_language/test_phi3v.py:119: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ tests/models/embedding/vision_language/test_phi3v.py:69: in _run_test check_embeddings_close( _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ def check_embeddings_close( *, embeddings_0_lst: Sequence[list[float]], embeddings_1_lst: Sequence[list[float]], name_0: str, name_1: str, tol: float = 1e-3, ) -> None: assert len(embeddings_0_lst) == len(embeddings_1_lst) for prompt_idx, (embeddings_0, embeddings_1) in enumerate( zip(embeddings_0_lst, embeddings_1_lst)): assert len(embeddings_0) == len(embeddings_1), ( f"Length mismatch: {len(embeddings_0)} vs. {len(embeddings_1)}") sim = F.cosine_similarity(torch.tenso...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tests/models/embedding/vision_language/test_phi3v.py` is failiing After installing vllm, run `pytest -sv tests/models/embedding/vision_language/test_phi3v.py::test_models_image[half-TIGER-Lab/VLM2Vec-Full]` A snippet of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unit test `tests/models/embedding/vision_language/test_phi3v.py` failing bug;help wanted;good first issue ### Your current environment ### 🐛 Describe the bug BUG: unittest `tests/models/embedding/vision_language/...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: f"Length mismatch: {len(embeddings_0)} vs. {len(embeddings_1)}")
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: f"Length mismatch: {len(embeddings_0)} vs. {len(embeddings_1)}")
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ng;model_support;multimodal_vlm;quantization attention;cuda;quantization;triton build_error;mismatch env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
