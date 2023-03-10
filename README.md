# Chatgpt 模型介绍以及API参数信息



## 1 Chatgpt API 参数 介绍。


`建议选择  `gpt-3.5-turbo`  便宜强大。`

> 使用 `tgpt-3.5-turbo` 模型

```bash
root@danliu:~# curl https://api.openai.com/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY'' \
  -d '{
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "Say this is a test!"}],
  "temperature": 0.7
}'
{"id":"chatcmpl-6sT4Heo3yFLW9BPp4chBtQA7sRdvc","object":"chat.completion","created":1678439469,"model":"gpt-3.5-turbo-0301","usage":{"prompt_tokens":13,"completion_tokens":7,"total_tokens":20},"choices":[{"message":{"role":"assistant","content":"\n\nThis is a test!"},"finish_reason":"stop","index":0}]}

```

> 使用 `text-davinci-003` 模型

```bash
root@danliu:~# curl https://api.openai.com/v1/completions \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
  "model": "text-davinci-003",
  "prompt": "Say this is a test",
  "max_tokens": 7,
  "temperature": 0
}'

{"id":"cmpl-6sT3DaVyLCm3xWRF11zQBaV5H8oZK","object":"text_completion","created":1678439403,"model":"text-davinci-003","choices":[{"text":"\n\nThis is indeed a test","index":0,"logprobs":null,"finish_reason":"length"}],"usage":{"prompt_tokens":5,"completion_tokens":7,"total_tokens":12}}

```




### 1.1 API 参数： 
| Request body  |类型 |  作用 |
|--|--|--|
| `model` |  string  Required |  选择模型，目前推荐使用`gpt-3.5-turbo`
| `prompt` | string or array | 发送提示场景 |
| `message` | array Required | 发送对话信息
| `temperature` | 默认 1 ， 设置温度 0-2的范围，值越低，回答越保守，值越大，回答越随机。|
| `top_p` | number Optional Defaults to 1 | 与 temperature 参数相似，推荐只使用 temperature 即可 |
| `n` | integer Optional Defaults to 1 | 每个对话回复生成几次 |
| `max_tokens` | integer Optional Defaults to 16 | 生成对话的字数的最大限制， 不超过 2048,新模型不超过4096 |
| suffix | string Optional Defaults to null | 文本完成后的后缀 |
| stream | boolean Optional Defaults to false | 是否以数据流的形式返回 |
|echo| boolean Optional Defaults to false | 是否将发送的问题一并返回 |
| stop | string or array Optional Defaults to null | 定义返回几次序列后，停止返回文字 |

`PS 标记部分重点关注`


## 2 模型分类以及价格：


| Models | Description | price  |
|--|--|--|
|GPT-3.5 | GPT-3的升级版，能够理解并生成自然语言以及代码| 	$0.002 / 1K tokens | 
| DALL·EBeta | 能够在自然语言的提示下生成以及编辑图形的模型 | 	$0.020 / image |
| WhisperBeta | 将语音转换成文本的模型 | $0.0004 / 1K tokens |
| Embeddings | 将文本转换成数字形式的模型 | 	$0.0004 / 1K tokens |
| CodexLimited beta |  能够理解并生成代码，包括将自然语言转换成代码 | 	
| Moderation |	微调过的模型能够理解文本是否存在敏感或者不安全 |
| GPT-3 | 能够理解并 | $0.0200 / 1K tokens |


### 2.1GPT-3.5
> GPT-3.5 能够理解并生成自然语言或者代码，` gpt-3.5-turbo `,是目前最强大并最有效率的模型，不仅能聊天，其他的任务也能完成。


| Latest model | Description |
|--|--|
| `gpt-3.5-turbo` | 经过优化后最强大的模型，价格只有 `text-davinci-003`的十分之一. 会根据我们的模型迭代不断升级。
| gpt-3.5-turbo-0301 | 2023年3月1日来自 gpt-3.5-turbo 的快照模型，不再升级，支持到2023年6月1日 | 
| text-davinci-003 | 	能够完成任何语言任务。与curie, babbage, or ada 模型，质量更好，输出时间更长，指令的遵循也更一致。还支持在文本中插入补语。 | 
| `text-davinci-002` |  与 text-davinci-003 的能力相似，但用监督下的微调而不是强化学习进行训练 |
| `code-davinci-002` | 	 对代码 完成任务 进行了优化 |


### 2.2 GPT-3
> GPT-3 自然语言模型

| Latest model |	Description |
|--|--|
| text-curie-001 | 能力很强，速度快，成本比 Davinci。|
| text-babbage-001	| 能够完成简单的任务，非常快，而且成本较低 |
| text-ada-001 | 	能够完成非常简单的任务，通常是GPT-3系列中最快的型号，而且成本最低。 |
| davinci	| 最有能力的GPT-3模型。可以完成其他型号所能完成的任何任务，通常质量更高。 |
| curie	| 能力很强，但比Davinci更快，成本更低。
|babbage | 能够完成简单的任务，速度非常快，而且成本较低 | 
| ada	| 能够完成非常简单的任务，通常是GPT-3系列中最快的型号，而且成本最低 |

### 2.3 Model endpoint compatability

| Model name | 	Endpoints |
|--|--|
| gpt-3.5-turbo | 	/v1/chat/completions|
| gpt-3.5-turbo-0301 |	/v1/chat/completions|
| text-davinci-003	| /v1/completions	|
|text-davinci-002	| /v1/completions`	|
|text-davinci-edit-001	| /v1/edits	|
|code-davinci-edit-001	| /v1/edits	|
|whisper-1	| /v1/audio/transcriptions, /v1/audio/translations |	
|text-curie-001	| /v1/completions	|
|text-babbage-001	| /v1/completions	|
|text-ada-001	| /v1/completions	|
|davinci	| /v1/completions, /v1/fine-tunes	|
|curie	| /v1/completions, /v1/fine-tunes	|
|babbage	| /v1/completions, /v1/fine-tunes	|
|ada	| /v1/completions, /v1/fine-tunes	|
|text-embedding-ada-002	| /v1/embeddings	|
|text-search-ada-doc-001 |	/v1/embeddings	|
|text-moderation-stable	 | /v1/moderations	|
| text-moderation-latest	| /v1/moderations |

