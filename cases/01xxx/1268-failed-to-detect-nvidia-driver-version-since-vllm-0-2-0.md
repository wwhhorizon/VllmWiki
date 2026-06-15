# vllm-project/vllm#1268: Failed to detect NVIDIA driver version since vllm 0.2.0

| 字段 | 值 |
| --- | --- |
| Issue | [#1268](https://github.com/vllm-project/vllm/issues/1268) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed to detect NVIDIA driver version since vllm 0.2.0

### Issue 正文摘录

Hey. I recently updated from 0.1.3 to 0.2.0. Since then I have a problem. The following Docker container is deployed through SageMaker: ``` FROM nvcr.io/nvidia/pytorch:22.12-py3 ARG DEBIAN_FRONTEND=noninteractive RUN apt-get -y update \ && apt-get -y install gcc \ && pip uninstall torch -y WORKDIR /app COPY requirements.txt . RUN pip install --no-cache-dir -r requirements.txt COPY . ``` ``` vllm==0.2.0 Flask==2.3.2 gunicorn==20.1.0 sentence_transformers==2.2.2 accelerate==0.23.0 huggingface_hub==0.17.3 typing-inspect==0.9.0 typing_extensions==4.8.0 ``` When creating the Inference service, CloudWatch then repeatedly spits out the following logs: ``` ============= == PyTorch == ============= NVIDIA Release 22.12 (build 49968248) PyTorch Version 1.14.0a0+410ce96 Container image Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES. All rights reserved. Copyright (c) 2014-2022 Facebook Inc. ... Copyright (c) 2013-2016 The Caffe contributors All rights reserved. Various files include modifications (c) NVIDIA CORPORATION & AFFILIATES. All rights reserved. This container image and its contents are governed by the NVIDIA Deep Learning Container License. By pulling and using the container, y...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Failed to detect NVIDIA driver version since vllm 0.2.0 Hey. I recently updated from 0.1.3 to 0.2.0. Since then I have a problem. The following Docker container is deployed through SageMaker: ``` FROM nvcr.io/nvidia/pyt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ==2.3.2 gunicorn==20.1.0 sentence_transformers==2.2.2 accelerate==0.23.0 huggingface_hub==0.17.3 typing-inspect==0.9.0 typing_extensions==4.8.0 ``` When creating the Inference service, CloudWatch then repeatedly spits o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
