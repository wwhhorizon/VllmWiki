# vllm-project/vllm#7650: [Bug]: Gemma2 models inference using vLLM 0.5.4 produces incorrect responses

| 字段 | 值 |
| --- | --- |
| Issue | [#7650](https://github.com/vllm-project/vllm/issues/7650) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;cuda;sampling |
| 症状 | crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma2 models inference using vLLM 0.5.4 produces incorrect responses

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using vLLM latest release (0.5.4). Installed "flashinfer" attention backend: https://github.com/flashinfer-ai/flashinfer/releases/download/v0.1.5/flashinfer-0.1.5+cu124torch2.4-cp310-cp310-linux_x86_64.whl The inference produces responses not related to prompt. ```python import uuid import json import logging import logging.config import os import yaml import traceback import subprocess from vllm import SamplingParams from vllm.entrypoints.llm import LLM from transformers import AutoTokenizer def init_logging(): logging.basicConfig(format='%(asctime)s [%(levelname)s] - [ProcessId %(process)d] %(name)s - %(message)s', level=logging.DEBUG) init_logging() log = logging.getLogger(__name__) os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_ALLOW_LONG_MAX_MODEL_LEN"] = "1" GEMMA2_27B_MODEL_PATH = "/home/ec2-user/SageMaker/gemma-2-27b-it" tokenizer = AutoTokenizer.from_pretrained(GEMMA2_27B_MODEL_PATH, trust_remote_code=True) eos_token = None tokenizer_config_json_path = os.path.join(GEMMA2_27B_MODEL_PATH, "tokenizer_config.json") with open(tokenizer_config_json_path, 'r') as f: tokenizer_config_json = json.load(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ment ### 🐛 Describe the bug I am using vLLM latest release (0.5.4). Installed "flashinfer" attention backend: https://github.com/flashinfer-ai/flashinfer/releases/download/v0.1.5/flashinfer-0.1.5+cu124torch2.4-cp310-cp3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma2 models inference using vLLM 0.5.4 produces incorrect responses bug;stale ### Your current environment ### 🐛 Describe the bug I am using vLLM latest release (0.5.4). Installed "flashinfer" attention backend:
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: te the *area under a curve* between two specific points. It results in a numerical value. * **Antiderivative:** An antiderivative of a function f(x) is a function F(x) whose derivative is f(x). * **Constant of Integrati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: # 🐛 Describe the bug I am using vLLM latest release (0.5.4). Installed "flashinfer" attention backend: https://github.com/flashinfer-ai/flashinfer/releases/download/v0.1.5/flashinfer-0.1.5+cu124torch2.4-cp310-cp310-linu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: attention_kv_cache;frontend_api;model_support;sampling_logits attention;cuda;sampling crash;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
