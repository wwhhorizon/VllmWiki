# vllm-project/vllm#17747: [Bug]: Issues with max_model_len and config_format mistral

| 字段 | 值 |
| --- | --- |
| Issue | [#17747](https://github.com/vllm-project/vllm/issues/17747) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issues with max_model_len and config_format mistral

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We have observed crashes and bad results when using the [mistralai/Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) model due to some bug in how `--max-model-len` is handled. For this model, the [params.json](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/blob/main/params.json) does not have any configuration for the max sequence length. The default value used is 128000 [REF](https://github.com/vllm-project/vllm/blob/de906b95f9d0b9669da902785a9012ac96edd578/vllm/transformers_utils/config.py#L689-L691). But, the HF config in [config.json](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/blob/main/config.json#L17) has `"max_position_embeddings": 131072`. So we run the OpenAI server with: ``` VLLM_USE_V1=1 VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve mistralai/Mistral-Small-3.1-24B-Instruct-2503 --tokenizer-mode mistral --config-format mistral --load-format mistral --max-num-seqs 4 --max-model-len 131072 ``` The server then boots with the expected warning (though it is a little misleading since we aren't using `config.json` and 128000 i...

## 现有链接修复摘要

#44286 [Bugfix] Fail fast or extend RoPE cache when VLLM_ALLOW_LONG_MAX_MODEL_LEN exceeds model positions

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Issues with max_model_len and config_format mistral bug ### Your current environment ### 🐛 Describe the bug We have observed crashes and bad results when using the [mistralai/Mistral-Small-3.1-24B-Instruct-2503](...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: not from the config): > WARNING 05-06 22:11:51 [config.py:3178] User-specified max_model_len (131072) is greater than the derived max_model_len (max_position_embeddings=128000 or model_max_length=None in model's config....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: have observed crashes and bad results when using the [mistralai/Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) model due to some bug in how `--max-model-len` i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: /pi/cpiayc7qwveqsg53w53ihzygo5qggdq4bzprcwvrqyu5eljbgt6z.py:37: unknown: block: [21452,0,0], thread: [53,0,0] Assertion `index out of bounds: 0 <= tl.broadcast_to(tmp10, [XBLOCK]) < 128000` failed. /home/vllm/.cache/vll...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: questions. correctness frontend_api;model_support cuda build_error;crash;mismatch env_dependency;memory_layout #44286 [Bugfix] Fail fast or extend RoPE cache when VLLM_ALLOW_LONG_MAX_MODEL_LEN exceeds model positions Yo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44286](https://github.com/vllm-project/vllm/pull/44286) | closes_keyword | 0.95 | [Bugfix] Fail fast or extend RoPE cache when VLLM_ALLOW_LONG_MAX_MODEL_LEN exceeds model positions | fix. - #17747 / #17777 / #17937 are Mistral `params.json` vs HF `config.json` length-derivation specifics, not the general env-override mismatch. - #18755 / #31662 are Nomic/`nom |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
