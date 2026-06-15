# vllm-project/vllm#7628: [Bug]: OpenGVLab/InternVL-Chat-V1-5 never stops properly

| 字段 | 值 |
| --- | --- |
| Issue | [#7628](https://github.com/vllm-project/vllm/issues/7628) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | install |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenGVLab/InternVL-Chat-V1-5 never stops properly

### Issue 正文摘录

### Your current environment latest released docker 0.5.4 on 8*H100 80GB on single GPU ### 🐛 Describe the bug Despite @DarkLight1337 closing this issue: https://github.com/vllm-project/vllm/issues/4393#issuecomment-2255638236 InternVL1-5 does not work properly. I've tried InternVL2-76 and it works, so there must be something slightly off. Maybe also issue is with InternVL2 just not always manifesting? So may be general bug. ```bash docker pull vllm/vllm-openai:latest docker stop 15b_vllm ; docker remove 15b_vllm docker run -d --restart=always \ --runtime=nvidia \ --gpus '"device=6"' \ --shm-size=10.24gb \ -p 23333:23333 \ -e NCCL_IGNORE_DISABLED_P2P=1 \ -v /etc/passwd:/etc/passwd:ro \ -v /etc/group:/etc/group:ro \ -u `id -u`:`id -g` \ -e VLLM_NCCL_SO_PATH=/usr/local/lib/python3.10/dist-packages/nvidia/nccl/lib/libnccl.so.2 \ -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \ -v "${HOME}"/.cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name 15b_vllm \ vllm/vllm-openai:latest \ --port=23333 \ --host=0.0.0.0 \ --model=OpenGVLab/InternVL-Chat-V1-5 \ --tensor-parallel-size=1 \ --seed 1234 \ --trust-remote-code \ --max-m...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: OpenGVLab/InternVL-Chat-V1-5 never stops properly bug ### Your current environment latest released docker 0.5.4 on 8*H100 80GB on single GPU ### 🐛 Describe the bug Despite @DarkLight1337 closing this issue: https...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 5 never stops properly bug ### Your current environment latest released docker 0.5.4 on 8*H100 80GB on single GPU ### 🐛 Describe the bug Despite @DarkLight1337 closing this issue: https://github.com/vllm-project/vllm/is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: base_url='http://FILLME/v1') from PIL import Image import base64 import requests from io import BytesIO prompt = "What tower do you see?" # The encoding function I linked previously - but we actually don't use this func...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .cache:$HOME/.cache/ -v "${HOME}"/.config:$HOME/.config/ -v "${HOME}"/.triton:$HOME/.triton/ \ --network host \ --name 15b_vllm \ vllm/vllm-openai:latest \ --port=23333 \ --host=0.0.0.0 \ --model=OpenGVLab/InternVL-Chat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: erly bug ### Your current environment latest released docker 0.5.4 on 8*H100 80GB on single GPU ### 🐛 Describe the bug Despite @DarkLight1337 closing this issue: https://github.com/vllm-project/vllm/issues/4393#issuecom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
