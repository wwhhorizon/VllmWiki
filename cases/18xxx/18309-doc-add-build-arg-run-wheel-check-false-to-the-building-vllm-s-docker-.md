# vllm-project/vllm#18309: [Doc]: add `--build-arg RUN_WHEEL_CHECK=false` to the "building-vllm-s-docker-image-from-source" section to avoid `check-wheel-size.py`-errors when building vllm for blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#18309](https://github.com/vllm-project/vllm/issues/18309) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: add `--build-arg RUN_WHEEL_CHECK=false` to the "building-vllm-s-docker-image-from-source" section to avoid `check-wheel-size.py`-errors when building vllm for blackwell

### Issue 正文摘录

### 📚 The doc issue According to https://docs.vllm.ai/en/stable/deployment/docker.html#building-vllm-s-docker-image-from-source > You can build and run vLLM from source via the provided [docker/Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile). To build vLLM: > > ``` > optionally specifies: --build-arg max_jobs=8 --build-arg nvcc_threads=2 > DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai --file docker/Dockerfile > ``` I did the following for Blackwell: ``` git clone https://github.com/vllm-project/vllm cd vllm/ git checkout tags/v0.9.0 -b mybranch DOCKER_BUILDKIT=1 sudo docker build . --target vllm-openai --tag my-vllm-openai --file docker/Dockerfile --build-arg max_jobs=4 --build-arg nvcc_threads=1 --build-arg torch_cuda_arch_list="12.0 12.1" ``` This resulted in the following issue: ``` [+] Building 2564.0s (32/41) docker:default => [internal] load build definition from Dockerfile 0.0s => => transferring dockerfile: 15.82kB 0.0s => WARN: FromAsCasing: 'as' and 'FROM' keywords' casing do not match (line 163) 0.0s => [internal] load metadata for docker.io/nvidia/cuda:12.8.1-devel-ubuntu20.04 2.0s => [internal] load metadata...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Doc]: add `--build-arg RUN_WHEEL_CHECK=false` to the "building-vllm-s-docker-image-from-source" section to avoid `check-wheel-size.py`-errors when building vllm for blackwell documentation;stale ### 📚 The doc issue Acc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ce" section to avoid `check-wheel-size.py`-errors when building vllm for blackwell documentation;stale ### 📚 The doc issue According to https://docs.vllm.ai/en/stable/deployment/docker.html#building-vllm-s-docker-image-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 0.4s => [base 6/12] RUN [base 7/12] RUN ldconfig /usr/local/cuda-$(echo 12.8.1 | cut -d. -f1,2)/compat/ 0.6s => [base 8/12] WORKDIR /workspace
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Doc]: add `--build-arg RUN_WHEEL_CHECK=false` to the "building-vllm-s-docker-image-from-source" section to avoid `check-wheel-size.py`-errors when building vllm for blackwell documentation;stale ### 📚 The doc issue Acc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eck-wheel-size.py`-errors when building vllm for blackwell documentation;stale ### 📚 The doc issue According to https://docs.vllm.ai/en/stable/deployment/docker.html#building-vllm-s-docker-image-from-source > You can bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
