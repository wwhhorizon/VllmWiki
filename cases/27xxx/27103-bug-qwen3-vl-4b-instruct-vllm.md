# vllm-project/vllm#27103: [Bug]: Qwen3-VL-4B-Instruct vllm推理报错

| 字段 | 值 |
| --- | --- |
| Issue | [#27103](https://github.com/vllm-project/vllm/issues/27103) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-4B-Instruct vllm推理报错

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 推理脚本： DISABLE_VERSION_CHECK=1 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python tools/vllm_infer.py \ --model_name_or_path /data/flux/zhanghang/weights/pretrained/Qwen3-VL-4B-Instruct \ --template qwen3_vl_nothink \ --pipeline_parallel_size 1 \ --dataset caption_image16_test_250821 \ --image_max_pixels 262144 \ --save_dir runs/caption/1017 报错完整： (Worker_TP0 pid=288155) ERROR 10-17 13:05:09 [multiproc_executor.py:671] Traceback (most recent call last): (Worker_TP0 pid=288155) ERROR 10-17 13:05:09 [multiproc_executor.py:671] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop (Worker_TP0 pid=288155) ERROR 10-17 13:05:09 [multiproc_executor.py:671] output = func(*args, **kwargs) (Worker_TP0 pid=288155) ERROR 10-17 13:05:09 [multiproc_executor.py:671] File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context (Worker_TP0 pid=288155) ERROR 10-17 13:05:09 [multiproc_executor.py:671] return func(*args, **kwargs) (Worker_TP0 pid=288155) ERROR 10-17 13:05:09 [multiproc_executor.py:671] File "/root/minico...

## 现有链接修复摘要

#29889 [Bugfix] respect user-defined flash attention version in ViT attentions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: g ### Your current environment ### 🐛 Describe the bug 推理脚本： DISABLE_VERSION_CHECK=1 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python tools/vllm_infer.py \ --model_name_or_path /data/flux/zhanghang/weights/pretrained/Qwen3-VL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-VL-4B-Instruct vllm推理报错 bug ### Your current environment ### 🐛 Describe the bug 推理脚本： DISABLE_VERSION_CHECK=1 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python tools/vllm_infer.py \ --model_name_or_path /data/fl
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nt environment ### 🐛 Describe the bug 推理脚本： DISABLE_VERSION_CHECK=1 CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python tools/vllm_infer.py \ --model_name_or_path /data/flux/zhanghang/weights/pretrained/Qwen3-VL-4B-Instruct \ -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency #29889 [Bugfix] respect user-defined flash attention version in ViT attentions Your curre...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 88155) ERROR 10-17 13:05:09 [multiproc_executor.py:671] out, softmax_lse = torch.ops._vllm_fa2_C.varlen_fwd( (Worker_TP0 pid=288155) ERROR 10-17 13:05:09 [multiproc_executor.py:671] File "/root/miniconda3/envs/vllm/lib/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29889](https://github.com/vllm-project/vllm/pull/29889) | closes_keyword | 0.95 | [Bugfix] respect user-defined flash attention version in ViT attentions | fix #27103, #25143, #17392, #28903 in better way. ## Test Plan Run `Qwen/Qwen3-VL-32B-Instruct` successfully with the default FA backend on H100. ```bash vllm serve Qwen/Qwen3-V |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
