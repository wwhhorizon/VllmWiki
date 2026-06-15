# vllm-project/vllm#39699: [Bug]: Loading of subdirectory safetensors get dispatched to `pt_weights_iterator`

| 字段 | 值 |
| --- | --- |
| Issue | [#39699](https://github.com/vllm-project/vllm/issues/39699) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Loading of subdirectory safetensors get dispatched to `pt_weights_iterator`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `DefaultModelLoader.load_weights` to support weight loading of model with subdirectories containing weights for model components, I used `allow_patterns_overrides = ["talker/model*.safetensors"]` to assign specific model weight to be loaded (confirmed that `.safetensors` exist locally), but got a pickle deserialization error. ```bash File "/repos/vllm-project/vllm/.venv/lib/python3.12/site-packages/torch/serialization.py", line 1855, in _legacy_load magic_number = pickle_module.load(f, **pickle_load_args) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/repos/vllm-project/vllm/.venv/lib/python3.12/site-packages/torch/_weights_only_unpickler.py", line 590, in load return Unpickler(file, encoding=encoding).load() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/repos/vllm-project/vllm/.venv/lib/python3.12/site-packages/torch/_weights_only_unpickler.py", line 544, in load self.append(self.memo[idx]) ~~~~~~~~~^^^^^ KeyError: 231 ``` After triaging, there's a bug that `_prepare_weights` ignores `allow_patterns_overrides` for a hardcoded safetensors pattern. https://github.com/vllm-project/vllm/blob/8d825b87d6590ca971823890f...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Loading of subdirectory safetensors get dispatched to `pt_weights_iterator` bug ### Your current environment ### 🐛 Describe the bug When using `DefaultModelLoader.load_weights` to support weight loading of model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: `allow_patterns_overrides = ["talker/model*.safetensors"]` to assign specific model weight to be loaded (confirmed that `.safetensors` exist locally), but got a pickle deserialization error. ```bash File "/repos/vllm-pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: corresponding pattern check silently fails, leaving `use_safetensors = False`. The downstream iterator to dispatch and select `pt_weights_iterator` on those safetensors files, causing a pickle deserialization error. ###...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Your current environment ### 🐛 Describe the bug When using `DefaultModelLoader.load_weights` to support weight loading of model with subdirectories containing weights for model components, I used `allow_patterns_overrid...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
