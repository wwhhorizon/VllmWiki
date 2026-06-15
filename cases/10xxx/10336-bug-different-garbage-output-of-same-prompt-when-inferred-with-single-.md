# vllm-project/vllm#10336: [Bug]: different garbage output of same prompt when inferred with single sequence vs concurrent requests on vllm openai server , temp =0.  (mixed batching in longrope))

| 字段 | 值 |
| --- | --- |
| Issue | [#10336](https://github.com/vllm-project/vllm/issues/10336) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: different garbage output of same prompt when inferred with single sequence vs concurrent requests on vllm openai server , temp =0.  (mixed batching in longrope))

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm version (latest was failing due to some issues like can not decode) : ```0.6.1.post1``` hosted the model : ``` CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server --model csp-phi-3-mini-128k-ft-outputs/qlora_merged_model_csp_phi-ckp-23850 --dtype bfloat16 --gpu-memory-utilization 0.9 --disable-log-requests --max-model-len 14000 ``` ```python import requests import json import time VLLM_INFER_URL = "http://0.0.0.0:8000/v1/completions" def infer_vllm(prompt:str,max_new_tokens = 800,temp=0.0) -> str: '''Infer from hosted vllm server''' payload = json.dumps({ "model": "csp-phi-3-mini-128k-ft-outputs/qlora_merged_model_csp_phi-ckp-23850", "prompt": prompt, "temperature": temp, # "top_k": 50, "top_p": 1, "max_tokens": max_new_tokens }) headers = { 'Content-Type': 'application/json' } try: status_code_failure = False start_time = time.time() response = requests.request("POST", VLLM_INFER_URL, headers=headers, data=payload) if response.status_code == 200: resp = json.loads(response.text)["choices"][0]["text"] return resp else: print(response.json()) return "None" from tqdm import...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: el csp-phi-3-mini-128k-ft-outputs/qlora_merged_model_csp_phi-ckp-23850 --dtype bfloat16 --gpu-memory-utilization 0.9 --disable-log-requests --max-model-len 14000 ``` ```python import requests import json import time VLL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e output of same prompt when inferred with single sequence vs concurrent requests on vllm openai server , temp =0. (mixed batching in longrope)) bug;stale ### Your current environment ### Model Input Dumps _No response_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm version (latest was failing due to some issues like can not decode) : ```0.6.1.post1``` hosted the model : ``` CUDA_VISIBLE_DEVICES=0 python3 -m vllm.ent...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: issues like can not decode) : ```0.6.1.post1``` hosted the model : ``` CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server --model csp-phi-3-mini-128k-ft-outputs/qlora_merged_model_csp_phi-ckp-23850 --d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ': 'application/json' } try: status_code_failure = False start_time = time.time() response = requests.request("POST", VLLM_INFER_URL, headers=headers, data=payload) if response.status_code == 200: resp = json.loads(resp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
