# vllm-project/vllm#11832: [Installation]: Qwen-VL-Chat kept returning out of vocabulary (OOV) error with docker deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#11832](https://github.com/vllm-project/vllm/issues/11832) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Qwen-VL-Chat kept returning out of vocabulary (OOV) error with docker deployment

### Issue 正文摘录

### How you are installing vllm Hi and I followed the sample code from PR #8029 to deploy Qwen-VL-Chat with vllm docker. While deployment was successful, I kept getting out of vocabulary OOV errors no matter how I test my inputs. My environment is Ubuntu 20.04 LTS, 2080Ti 22G x2, Docker deployment was successful for Qwen2-VL-7B and Qwen2.5:32b so it should not be configuration issue. How I deployed: ``` sudo docker run --runtime nvidia --gpus '"device=0,1"' --ipc=host -p 18434:8000 -v hf_cache:/root/.cache/huggingface -d -e HF_ENDPOINT=https://hf-mirror.com -e HF_HUB_ENABLE_HF_TRANSFER=0 --name Qwen-VL-Chat vllm/vllm-openai:latest --model Qwen/Qwen-VL-Chat --tokenizer Qwen/Qwen-VL-Chat --tensor-parallel-size 2 --trust-remote-code --chat-template examples/template_chatml.jinja --dtype='half' ``` Error msg: ``` Error in API call: 400 {"object":"error","message":"Token id 151859 is out of vocabulary","type":"BadRequestError","param":null,"code":400} ``` Test code: ``` import requests import base64 import time # Function to encode the image to base64 def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).decode("utf-8") def...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Installation]: Qwen-VL-Chat kept returning out of vocabulary (OOV) error with docker deployment installation ### How you are installing vllm Hi and I followed the sample code from PR #8029 to deploy Qwen-VL-Chat with v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Qwen-VL-Chat kept returning out of vocabulary (OOV) error with docker deployment installation ### How you are installing vllm Hi and I followed the sample code from PR #8029 to deploy Qwen-VL-Chat with vl
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ect":"error","message":"Token id 151859 is out of vocabulary","type":"BadRequestError","param":null,"code":400} ``` Test code: ``` import requests import base64 import time # Function to encode the image to base64 def e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: --trust-remote-code --chat-template examples/template_chatml.jinja --dtype='half' ``` Error msg: ``` Error in API call: 400 {"object":"error","message":"Token id 151859 is out of vocabulary","type":"BadRequestError","pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: print() if __name__ == "__main__": main() ``` I tried to search the whole observable web and could not find any similar case. So I'm replying here for possible help. Much appreciated! ### Before submitting a new issue.....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
