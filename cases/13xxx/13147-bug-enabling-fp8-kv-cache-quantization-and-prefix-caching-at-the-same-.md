# vllm-project/vllm#13147: [Bug]: Enabling fp8 KV cache quantization and prefix caching at the same time on Radeon (W7900/RDNA3) crashes the process

| 字段 | 值 |
| --- | --- |
| Issue | [#13147](https://github.com/vllm-project/vllm/issues/13147) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enabling fp8 KV cache quantization and prefix caching at the same time on Radeon (W7900/RDNA3) crashes the process

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Server command line: ```bash python -O -u -m vllm.entrypoints.openai.api_server --host=0.0.0.0 --port=8000 \ --model ~/models/Qwen2.5-72B-Instruct-GPTQ-Int8/ \ --served-model-name Qwen\ 2.5\ 72B \ --enable-prefix-caching \ --tensor-parallel-size 2 \ --kv-cache-dtype fp8 ``` Client command line (run twice): ```bash curl localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{"model": "Qwen 2.5 72B", "messages": [{"role": "user", "content": "Test"}]}' ``` Error message: ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e5',)") Either removing `--enable-prefix-caching` or `--kv-cache-dtype fp8` solves the problem ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding atten...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Enabling fp8 KV cache quantization and prefix caching at the same time on Radeon (W7900/RDNA3) crashes the process bug ### Your current environment ### 🐛 Describe the bug Server command line: ```bash python -O -u...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Enabling fp8 KV cache quantization and prefix caching at the same time on Radeon (W7900/RDNA3) crashes the process bug ### Your current environment ### 🐛 Describe the bug Server command line: ```bash python -O -u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: "}]}' ``` Error message: ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e5',)") Either removing `--enable-prefix-caching` or `--kv-cache-dtype fp8` solves the problem ###...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -m vllm.entrypoints.openai.api_server --host=0.0.0.0 --port=8000 \ --model ~/models/Qwen2.5-72B-Instruct-GPTQ-Int8/ \ --served-model-name Qwen\ 2.5\ 72B \ --enable-prefix-caching \ --tensor-parallel-size 2 \ --kv-cache-...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13147">#13147</a></li> </ul> <h4>Fixes</h4> <ul> <li>Preserve <code>RootModel</code> core metadata by <a href="https… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13147">#13147</a></li> </ul> <h4>Fixes</h4> <ul> <li>Preserve <code>RootModel</code> core metadata by <a href="https… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13147">#13147</a></li> </ul> <h4>Fixes</h4> <ul> <li>Preserve <code>RootModel</code> core metadata by <a href="https… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13147">#13147</a></li> </ul> <h4>Fixes</h4> <ul> <li>Preserve <code>RootModel</code> core metadata by <a href="https… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | in <a href="https://redirect.github.com/pydantic/pydantic/pull/13147">#13147</a></li> </ul> <h4>Fixes</h4> <ul> <li>Preserve <code>RootModel</code> core metadata by <a href="https… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
