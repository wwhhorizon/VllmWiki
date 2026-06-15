# vllm-project/vllm#34728: [Bug]: Nemotron NVFP4 Failing With TRTLLM NVFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#34728](https://github.com/vllm-project/vllm/issues/34728) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Nemotron NVFP4 Failing With TRTLLM NVFP4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - launch ```bash vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --enforce-eager --port 8003 --trust-remote-code ``` - stack trace ``` (vllm) robertgshaw2-redhat@dgx-b200-02:~/vllm$ vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --enforce-eager --port 8003 --trust-remote-code Reserved 1 GPU(s): [2] for command execution (APIServer pid=297715) INFO 02-17 12:31:22 [utils.py:293] (APIServer pid=297715) INFO 02-17 12:31:22 [utils.py:293] █ █ █▄ ▄█ (APIServer pid=297715) INFO 02-17 12:31:22 [utils.py:293] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.16.0rc2.dev107+g48134a2c2 (APIServer pid=297715) INFO 02-17 12:31:22 [utils.py:293] █▄█▀ █ █ █ █ model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 (APIServer pid=297715) INFO 02-17 12:31:22 [utils.py:293] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer pid=297715) INFO 02-17 12:31:22 [utils.py:293] (APIServer pid=297715) INFO 02-17 12:31:22 [utils.py:229] non-default args: {'model_tag': 'nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4', 'port': 8003, 'model': 'nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4', 'trust_remote_code': True, 'enforce_eager': True} (APIServer pid=297715) The argument `trust_remote_code` is...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: Nemotron NVFP4 Failing With TRTLLM NVFP4 bug ### Your current environment ### 🐛 Describe the bug - launch ```bash vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --enforce-eager --port 8003 --trust-remote-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: 3, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d=297715) INFO 02-17 12:31:22 [utils.py:293] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.16.0rc2.dev107+g48134a2c2 (APIServer pid=297715) INFO 02-17 12:31:22 [utils.py:293] █▄█▀ █ █ █ █ model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: -trust-remote-code ``` - stack trace ``` (vllm) robertgshaw2-redhat@dgx-b200-02:~/vllm$ vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --enforce-eager --port 8003 --trust-remote-code Reserved 1 GPU(s): [2] for c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: Server pid=297715) INFO 02-17 12:31:23 [config.py:500] Setting attention block size to 4176 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=297715) INFO 02-17 12:31:23 [config.py:531] Pad...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
