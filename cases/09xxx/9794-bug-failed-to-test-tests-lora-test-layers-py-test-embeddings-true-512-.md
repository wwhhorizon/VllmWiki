# vllm-project/vllm#9794: [Bug]: failed to test tests/lora/test_layers.py::test_embeddings[True-512-cuda:1-1]

| 字段 | 值 |
| --- | --- |
| Issue | [#9794](https://github.com/vllm-project/vllm/issues/9794) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf;nondeterministic |
| 根因提示 | env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: failed to test tests/lora/test_layers.py::test_embeddings[True-512-cuda:1-1]

### Issue 正文摘录

### Your current environment ### Model Input Dumps None ### 🐛 Describe the bug - pytest tests/lora/test_layers.py::test_embeddings[True-512-cuda:0-1]: **passed** - pytest tests/lora/test_layers.py::test_embeddings[True-512-cuda:1-1]: **failed** seems that DummyLoRAManager().init_random_lora puts lora weight on the wrong device, error msg: ```bash =========================================================================================== test session starts =========================================================================================== platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0 rootdir: /root/vllm configfile: pyproject.toml plugins: anyio-4.6.2.post1 collected 1 item tests/lora/test_layers.py F [100%] ================================================================================================ FAILURES ================================================================================================= ___________________________________________________________________________________ test_embeddings[True-512-cuda:1-1] ____________________________________________________________________________________ dist_init = None, num_loras = 1, device = 'cuda:1',...

## 现有链接修复摘要

#10223 [Misc][LoRA] Replace hardcoded cuda device with configurable argument

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: ified by :attr:`padding_idx` are expected to differ from the numerical ones. .. note:: Note that `:class:`torch.nn.Embedding` differs from this function in that it initializes the row of :attr:`weight` specified by :att...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: bedding = create_random_embedding_layer() lora_embedding.set_mapping(punica_wrapper) lora_dict, _ = populate_loras( id_to_index, layer=lora_embedding, layer_weights=embedding.weight.T, ) input
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tion with respect to entries in :attr:`weight` at the row specified by :attr:`padding_idx` are expected to differ from the numerical ones. .. note:: Note that `:class:`torch.nn.Embedding` differs from this function in t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: max_lora_rank=8, lora_dtype=torch.float16) def create_random_embedding_layer(): embedding = VocabParallelEmbedding(vocab_size, 256) embedding.weight.data = torch.rand_like(embedding.weight.data)
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Bug]: failed to test tests/lora/test_layers.py::test_embeddings[True-512-cuda:1-1] bug ### Your current environment ### Model Input Dumps None ### 🐛 Describe the bug - pytest tests/lora/test_layers.py::test_embeddings[T...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10223](https://github.com/vllm-project/vllm/pull/10223) | closes_keyword | 0.95 | [Misc][LoRA] Replace hardcoded cuda device with configurable argument  | FIX #9794 (*link existing issues this PR will resolve*) This PR replaces the hardcoded CUDA device with a configurable argument, which not only makes the code more flexible b |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
