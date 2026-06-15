# vllm-project/vllm#32399: [Bug]: High Rate of endless Decoding in DeepSeekV3.2 Inference with vLLM v0.13.0

| 字段 | 值 |
| --- | --- |
| Issue | [#32399](https://github.com/vllm-project/vllm/issues/32399) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: High Rate of endless Decoding in DeepSeekV3.2 Inference with vLLM v0.13.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **My launch command is:** ``` VLLM_USE_DEEP_GEMM=0 vllm serve /models/DeepSeek-V3.2 --tensor-parallel-size 2 --data-parallel-size 4 --served-model-name deepseek_v3_2_t --enable-auto-tool-choice --tool-call-parser deepseek_v32 --reasoning-parser deepseek_v3 --tokenizer-mode deepseek_v32 --max-num-seqs 512 --max-model-len 131072 --speculative-config '{"method":"deepseek_mtp","num_speculative_tokens":1}' --attention-backend FLASHMLA_SPARSE --kv-cache-dtype fp8 ``` **My performance pressure test script is:** ``` from transformers import AutoTokenizer import json, aiohttp, time, math, asyncio, traceback from typing import List, Optional, Dict import sys, os sys.path.append("/models/DeepSeek-V3.2/encoding") from encoding_dsv32 import encode_messages class RequestSender: @staticmethod def _create_session(openai_url: str): conn = aiohttp.TCPConnector(limit=0, ttl_dns_cache=None) timeout = aiohttp.ClientTimeout(total=None) return aiohttp.ClientSession( connector=conn, timeout=timeout, base_url=openai_url, raise_for_status=True ) @staticmethod async def _get_result(tokenizer, session, model_name: str, messages: List[Dict[str, str]], max_to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: p8 ``` **My performance pressure test script is:** ``` from transformers import AutoTokenizer import json, aiohttp, time, math, asyncio, traceback from typing import List, Optional, Dict import sys, os sys.path.append("...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: the bug **My launch command is:** ``` VLLM_USE_DEEP_GEMM=0 vllm serve /models/DeepSeek-V3.2 --tensor-parallel-size 2 --data-parallel-size 4 --served-model-name deepseek_v3_2_t --enable-auto-tool-choice --tool-call-parse...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Rate of endless Decoding in DeepSeekV3.2 Inference with vLLM v0.13.0 bug;stale ### Your current environment ### 🐛 Describe the bug **My launch command is:** ``` VLLM_USE_DEEP_GEMM=0 vllm serve /models/DeepSeek-V3.2 --te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ckend FLASHMLA_SPARSE --kv-cache-dtype fp8 ``` **My performance pressure test script is:** ``` from transformers import AutoTokenizer import json, aiohttp, time, math, asyncio, traceback from typing import List, Optiona...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m_speculative_tokens":1}' --attention-backend FLASHMLA_SPARSE --kv-cache-dtype fp8 ``` **My performance pressure test script is:** ``` from transformers import AutoTokenizer import json, aiohttp, time, math, asyncio, tr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
