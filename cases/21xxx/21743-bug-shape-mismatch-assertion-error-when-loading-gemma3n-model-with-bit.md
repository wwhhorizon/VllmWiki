# vllm-project/vllm#21743: [Bug]: Shape mismatch assertion error when loading Gemma3n model with BitsAndBytes quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#21743](https://github.com/vllm-project/vllm/issues/21743) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Shape mismatch assertion error when loading Gemma3n model with BitsAndBytes quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description:** Fails to load Gemma3n models with BitsAndBytes quantization due to a shape mismatch assertion error in the linear layer weight loader. **Error Log:** ```text (venv) [ec2-user@ip-10-25-180-35 engine]$ python test.py /home/ec2-user/venv/lib64/python3.9/site-packages/networkx/utils/backends.py:135: RuntimeWarning: networkx backend defined more than once: nx-loopback backends.update(_get_backends("networkx.backends")) INFO 07-28 10:44:49 [__init__.py:235] Automatically detected platform cuda. INFO 07-28 10:44:53 [utils.py:326] non-default args: {'model': 'unsloth/gemma-3n-E4B-it-unsloth-bnb-4bit', 'trust_remote_code': True, 'dtype': torch.bfloat16, 'max_model_len': 4000, 'gpu_memory_utilization': 0.6, 'disable_log_stats': True, 'quantization': 'bitsandbytes', 'enforce_eager': True} WARNING 07-28 10:44:53 [config.py:531] The global random seed is set to 0. Since VLLM_ENABLE_V1_MULTIPROCESSING is set to False, this may affect the random state of the Python process that launched vLLM. INFO 07-28 10:45:01 [config.py:952] Resolved `--runner auto` to `--runner generate`. Pass the value explicitly to silence this message. I...

## 现有链接修复摘要

#21808 [Bugfix] Fix shape mismatch assertion error when loading Gemma3n model with BitsAndBytes quantization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 52] Resolved `--runner auto` to `--runner generate`. Pass the value explicitly to silence this message. INFO 07-28 10:45:01 [config.py:1001] Resolved `--convert auto` to `--convert none`. Pass the value explicitly to si...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: est.py /home/ec2-user/venv/lib64/python3.9/site-packages/networkx/utils/backends.py:135: RuntimeWarning: networkx backend defined more than once: nx-loopback backends.update(_get_backends("networkx.backends")) INFO 07-2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: pe mismatch assertion error when loading Gemma3n model with BitsAndBytes quantization bug ### Your current environment ### 🐛 Describe the bug **Description:** Fails to load Gemma3n models with BitsAndBytes quantization...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Shape mismatch assertion error when loading Gemma3n model with BitsAndBytes quantization bug ### Your current environment ### 🐛 Describe the bug **Description:** Fails to load Gemma3n models with BitsAndBytes qua...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: Shape mismatch assertion error when loading Gemma3n model with BitsAndBytes quantization bug ### Your current environment ### 🐛 Describe the bug **Description:** Fails to load Gemma3n models with BitsAndBytes qua...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21808](https://github.com/vllm-project/vllm/pull/21808) | closes_keyword | 0.95 | [Bugfix] Fix shape mismatch assertion error when loading Gemma3n model with BitsAndBytes quantization | Fix #21743 ## Test Plan ```python import torch from vllm import LLM, SamplingParams model_path = "unsloth/gemma-3n-E4B-it-unsloth-bnb-4bit" llm = LLM( model=model_path, t |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
