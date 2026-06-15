# vllm-project/vllm#19810: Revert "[CI] Update FlashInfer to 0.2.6.post1" --- edit: No, better add "12.0" to FlashInfer TORCH_CUDA_ARCH_LIST see PR #19794

| 字段 | 值 |
| --- | --- |
| Issue | [#19810](https://github.com/vllm-project/vllm/issues/19810) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | kernel;operator;sampling |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Revert "[CI] Update FlashInfer to 0.2.6.post1" --- edit: No, better add "12.0" to FlashInfer TORCH_CUDA_ARCH_LIST see PR #19794

### Issue 正文摘录

The Pullrequest https://github.com/vllm-project/vllm/pull/19297 broke SM 120 Blackwell compability (RTX 50xx, RTX PRO). You can't use `-e VLLM_USE_FLASHINFER_SAMPLER=1` anymore (which is the default) and need to fall back to `-e VLLM_USE_FLASHINFER_SAMPLER=0` which will give you less performance and this warning: > WARNING 06-18 08:55:01 [topk_topp_sampler.py:52] FlashInfer is available, but it is not enabled. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please set VLLM_USE_FLASHINFER_SAMPLER=1. I did 2 builds, both with `--build-arg torch_cuda_arch_list='12.0` (SM 120 compatible only) and pushed them to Docker hub: 1. `wurstdeploy/vllm:azure10thjunesolo120` which is based on the last commit of 10th June (da9b523ce1fd5c27bfd18921ba0388bf2e8e4618) and which still uses the old FlashInfer version ``` git checkout -b 10thjune da9b523ce1fd5c27bfd18921ba0388bf2e8e4618 DOCKER_BUILDKIT=1 sudo docker build --build-arg max_jobs=64 --build-arg USE_SCCACHE=0 --build-arg GIT_REPO_CHECK=1 --build-arg CUDA_VERSION=12.8.1 --build-arg torch_cuda_arch_list='12.0' --build-arg RUN_WHEEL_CHECK=false --tag wurstdeploy/vllm:azure10thjunesolo120 -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Revert "[CI] Update FlashInfer to 0.2.6.post1" --- edit: No, better add "12.0" to FlashInfer TORCH_CUDA_ARCH_LIST see PR #19794 The Pullrequest https://github.com/vllm-project/vllm/pull/19297 broke SM 120 Blackwell comp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nfer to 0.2.6.post1" --- edit: No, better add "12.0" to FlashInfer TORCH_CUDA_ARCH_LIST see PR #19794 The Pullrequest https://github.com/vllm-project/vllm/pull/19297 broke SM 120 Blackwell compability (RTX 50xx, RTX PRO...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: can run via sudo docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 \ -e VLLM_USE_FLASHINFER_SAMPLER=1 \ wurstdeploy/vllm:azure10thjunesolo120 --model Qwen/Qwen3-0.6B ``...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: --build-arg torch_cuda_arch_list='12.0' --build-arg RUN_WHEEL_CHECK=false --tag wurstdeploy/vllm:azure10thjunesolo120 --target vllm-openai --progress plain -f docker/Dockerfile . # this is still SM 120 compatible, you c...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ll give you less performance and this warning: > WARNING 06-18 08:55:01 [topk_topp_sampler.py:52] FlashInfer is available, but it is not enabled. Falling back to the PyTorch-native implementation of top-p & top-k sampli...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
