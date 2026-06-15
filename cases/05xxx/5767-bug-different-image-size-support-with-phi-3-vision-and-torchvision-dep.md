# vllm-project/vllm#5767: [Bug]: Different Image Size support with Phi-3-Vision and torchvision dependency

| 字段 | 值 |
| --- | --- |
| Issue | [#5767](https://github.com/vllm-project/vllm/issues/5767) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Different Image Size support with Phi-3-Vision and torchvision dependency

### Issue 正文摘录

### Your current environment I encountered a few issues while running phi-3-vision with the vllm built from current main branch. 1. Dependency: `torchvision` is a dependency under [image_processing_phi3_v.py](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct/blob/main/image_processing_phi3_v.py) Currently it is only included in requirements-test.txt, not requirements-common.txt. But importing the image processor also needs `torchvision` be available during imports. 2. Different Image Size Support I have built a vllm docker based on the latest main branch. I have the following script to resize the `stop_sign.jpg` before sending to vllm API server. ```text python send_phi3v_request.py ``` ```python import base64 import requests import time import random import numpy as np # To calculate the mean import json import os from PIL import Image # Parameters num_iterations = 20 # Number of times to repeat the request # To store latencies for each iteration latencies = [] ttfts = [] output_processing_times = [] output_throughputs = [] # Function to encode the image def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Different Image Size support with Phi-3-Vision and torchvision dependency bug ### Your current environment I encountered a few issues while running phi-3-vision with the vllm built from current main branch. 1. De...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `torchvision` is a dependency under [image_processing_phi3_v.py](https://huggingface.co/microsoft/Phi-3-vision-128k-instruct/blob/main/image_processing_phi3_v.py) Currently it is only included in requirements-test.txt,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: _sign.jpg` before sending to vllm API server. ```text python send_phi3v_request.py ``` ```python import base64 import requests import time import random import numpy as np # To calculate the mean import json import os f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: processing_phi3_v.py) Currently it is only included in requirements-test.txt, not requirements-common.txt. But importing the image processor also needs `torchvision` be available during imports. 2. Different Image Size...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/opt/conda/envs/vllm/lib/python3.11/site-packages/torch/utils/_contextlib...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
