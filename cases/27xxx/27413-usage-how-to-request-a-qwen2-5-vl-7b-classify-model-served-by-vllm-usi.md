# vllm-project/vllm#27413: [Usage]: how to request a qwen2.5-VL-7B classify model served by vllm using openai SDK?

| 字段 | 值 |
| --- | --- |
| Issue | [#27413](https://github.com/vllm-project/vllm/issues/27413) |
| 状态 | closed |
| 标签 | good first issue;usage;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to request a qwen2.5-VL-7B classify model served by vllm using openai SDK?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I launch a server with the following command to serving a Qwen2.5-VL-7B model finetued for seqence classification. (this model replaced the lm_head with a 2 classes score_head) The launch command is : ``` vllm serve --model=//video_classification/qwenvl_7b_video_cls/v5-20251011-121851/2340_vllm_format --served_model_name Qwen2.5-7B-shenhe --task=classify --port=8080 --tensor-parallel-size=2 ``` I don't know how to request the server with the openAI sdk. I use the code snnipet showed below which works well with pure text, but it got 400 bad request when I put the video url into the prompt this works well: ``` # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project """Example Python client for classification API using vLLM API server NOTE: start a supported classification model server with `vllm serve`, e.g. vllm serve jason9693/Qwen2.5-1.5B-apeach """ import argparse import pprint import requests def post_http_request(payload: dict, api_url: str) -> requests.Response: headers = {"User-Agent": "Test Client"} response = r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: how to request a qwen2.5-VL-7B classify model served by vllm using openai SDK? good first issue;usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: how to request a qwen2.5-VL-7B classify model served by vllm using openai SDK? good first issue;usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ith `vllm serve`, e.g. vllm serve jason9693/Qwen2.5-1.5B-apeach """ import argparse import pprint import requests def post_http_request(payload: dict, api_url: str) -> requests.Response: headers = {"User-Agent": "Test C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: dict, api_url: str) -> requests.Response: headers = {"User-Agent": "Test Client"} response = requests.post(api_url, headers=headers, json=payload) return response def parse_args(): parse = argparse.ArgumentParser() pars...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
