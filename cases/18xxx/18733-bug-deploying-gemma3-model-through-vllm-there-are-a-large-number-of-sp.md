# vllm-project/vllm#18733: [Bug]: Deploying Gemma3 model through VLLM, there are a large number of special characters <pad> filled in the reply content

| 字段 | 值 |
| --- | --- |
| Issue | [#18733](https://github.com/vllm-project/vllm/issues/18733) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deploying Gemma3 model through VLLM, there are a large number of special characters <pad> filled in the reply content

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After deploying the Gemma3 model of 4b using VLLM, when accessed through interface v1/cat/completeness, the reply content is only filled with a large number of special characters . The specific environmental parameters are listed above. The test code is below. ```python import requests import json class LLMTester: def __init__(self, base_url: str = "http://10.0.82.212:8088"): self.base_url = base_url def test_chat_completion(self, prompt: str, image_url: str = None): """测试聊天完成接口""" headers = { "Content-Type": "application/json" } # 构建消息内容 message_content = [] if prompt: message_content.append({ "type": "text", "text": prompt }) data = { "model": "gemma-3-4b-it", "messages": [ { "role": "user", "content": message_content } ], "max_tokens": 512, "temperature": 0.5, "top_p": 0.95, "top_k": 50, "skip_special_tokens": False } try: response = requests.post(f"{self.base_url}/v1/chat/completions", headers=headers, json=data) print(f"Response: {response.text}") except Exception as e: print(f"Error: {str(e)}") def main(): tester = LLMTester() # 测试纯文本输入 prompt = "who are you ? " tester.test_chat_completion(prompt) if __name__ == "__main__":...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ug]: Deploying Gemma3 model through VLLM, there are a large number of special characters <pad> filled in the reply content bug ### Your current environment ### 🐛 Describe the bug After deploying the Gemma3 model of 4b u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Deploying Gemma3 model through VLLM, there are a large number of special characters <pad> filled in the reply content bug ### Your current environment ### 🐛 Describe the bug After deploying the Gemma3 model of 4b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: : CUDA_VISIBLE_DEVICES=6 \ vllm serve \ --host 0.0.0.0 \ --port 8088 \ --dtype float16 \ --served-model-name gemma-3-4b-it \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --tokenizer /home/jdli/models/gemma-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion(prompt) if __name__ == "__main__": main() ``` vllm command: CUDA_VISIBLE_DEVICES=6 \ vllm serve \ --host 0.0.0.0 \ --port 8088 \ --dtype float16 \ --served-model-name gemma-3-4b-it \ --tensor-parallel-size 1 \ --gp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: l parameters are listed above. The test code is below. ```python import requests import json class LLMTester: def __init__(self, base_url: str = "http://10.0.82.212:8088"): self.base_url = base_url def test_chat_complet...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
