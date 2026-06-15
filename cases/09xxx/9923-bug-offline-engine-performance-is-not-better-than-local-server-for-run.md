# vllm-project/vllm#9923: [Bug]: Offline engine performance is not better than local server for running batch

| 字段 | 值 |
| --- | --- |
| Issue | [#9923](https://github.com/vllm-project/vllm/issues/9923) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Offline engine performance is not better than local server for running batch

### Issue 正文摘录

### Your current environment ### Model Input Dumps ### 🐛 Describe the bug I'm running some benchmarks to test using the offline engine for batch processing Llama 405B ( `sglang.Engine.generate()` ) vs. spinning up a server and running the same batch of requests locally against that live SGLang server. ### Local server batch benchmark: - First, boot up a local server with `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 --tp 8 --mem-fraction-static 0.8 --port 8001` - Next, I ran the following script ``` import json import time import requests from typing import Dict, Any, List import torch from tqdm import tqdm from multiprocessing import Pool, cpu_count def process_single_request(request: Dict[str, Any]) -> Dict[str, Any]: try: response = requests.post( "http://localhost:8001/v1/chat/completions", json=request['body'] ) response.raise_for_status() response_data = response.json() # Format result processed_result = { "id": f"cmpl-{response_data['id']}", "custom_id": request['custom_id'], "response": { "choices": [{ "message": { "role": "assistant", "content": response_data["choices"][0]["message"]["content...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ction-static 0.8 --port 8001` - Next, I ran the following script ``` import json import time import requests from typing import Dict, Any, List import torch from tqdm import tqdm from multiprocessing import Pool, cpu_co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: g.launch_server --model-path meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 --tp 8 --mem-fraction-static 0.8 --port 8001` - Next, I ran the following script ``` import json import time import requests from typing import Di...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: local server for running batch bug ### Your current environment ### Model Input Dumps ### 🐛 Describe the bug I'm running some benchmarks to test using the offline engine for batch processing Llama 405B ( `sglang.Engine....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Local server batch benchmark: - First, boot up a local server with `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 -m sglang.launch_server --model-path meta-llama/Meta-Llama-3.1-405B-Instruct-FP8 --tp 8 --mem-fraction...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ine.generate()` ) vs. spinning up a server and running the same batch of requests locally against that live SGLang server. ### Local server batch benchmark: - First, boot up a local server with `CUDA_VISIBLE_DEVICES=0,1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
